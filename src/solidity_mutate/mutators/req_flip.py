import re
import shutil

from .common import Colors, color


_COMPARE_RE = re.compile(r"(>=|<=|==|!=|>|<)")
_STRING_RE = re.compile(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'')


def _operator_matches_outside_strings(line):
    string_ranges = [match.span() for match in _STRING_RE.finditer(line)]

    for match in _COMPARE_RE.finditer(line):
        start, end = match.span()
        if any(start >= s and end <= e for s, e in string_ranges):
            continue
        yield match


def mutate_req_flip(ctx):
    with open(ctx.target_file) as f:
        lines = f.read().split("\n")

    total = compiled = caught = timeouts = 0
    name = "REQ-FLIP"
    flips = {
        "==": "!=",
        "!=": "==",
        ">": "<",
        "<": ">",
        ">=": "<=",
        "<=": ">=",
    }

    if ctx.should_print_sections():
        print(color("\n--- REQ-FLIP (Require/Assert Condition Flip) ---", Colors.CYAN))

    for i, line in enumerate(lines):
        if ("require" not in line) and ("assert" not in line):
            continue

        for m in _operator_matches_outside_strings(line):
            total += 1
            start, end = m.span()
            op = m.group()
            new_op = flips[op]

            mutated = lines.copy()
            mutated[i] = line[:start] + new_op + line[end:]

            with open(ctx.target_file, "w") as f:
                f.write("\n".join(mutated))

            output, timed_out = ctx.run_forge(ctx.run_timeout_seconds)
            status, compiled, caught = ctx.process_result(output, compiled, caught, timed_out)
            if timed_out:
                timeouts += 1

            if ctx.should_print_mutants():
                print(ctx.render_mutant_line(name, i + 1, line.strip(), mutated[i].strip(), status, timed_out))

            if "Uncaught" in status:
                ctx.uncaught_by_category["Require/Assert VALIDATION"] += 1

            shutil.copy(ctx.backup_file, ctx.target_file)

    ctx.print_summary(name, total, compiled, caught, timeouts)
    return total, compiled, caught, timeouts
