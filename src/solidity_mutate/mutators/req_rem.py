import shutil

from .common import Colors, color, scan_source


def mutate_req_rem(ctx):
    with open(ctx.target_file) as f:
        lines = f.read().split("\n")
    scan = scan_source(lines)

    total = compiled = caught = timeouts = 0
    name = "REQ-RM"

    if ctx.should_print_sections():
        print(color("\n--- REQ-REM (Require/Assert Removal) ---", Colors.CYAN))

    for i, line in enumerate(lines):
        code_line = scan.masked_lines[i]
        if ("require" not in code_line) and ("assert" not in code_line):
            continue

        total += 1
        mutated = lines.copy()
        comment_start = scan.comment_starts[i]
        if comment_start is None:
            mutated[i] = "uint256 _ = 0;"
        else:
            mutated[i] = "uint256 _ = 0;" + line[comment_start:]

        with open(ctx.target_file, "w") as f:
            f.write("\n".join(mutated))

        output, timed_out = ctx.run_forge(ctx.run_timeout_seconds)
        status, compiled, caught = ctx.process_result(output, compiled, caught, timed_out)
        if timed_out:
            timeouts += 1

        if ctx.should_print_mutants():
            print(ctx.render_mutant_line(name, i + 1, line.strip(), "uint256 _ = 0;", status, timed_out))

        if "Uncaught" in status:
            ctx.uncaught_by_category["Require/Assert VALIDATION"] += 1

        shutil.copy(ctx.backup_file, ctx.target_file)

    ctx.print_summary(name, total, compiled, caught, timeouts)
    return total, compiled, caught, timeouts
