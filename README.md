# solidity-mutate

Mutation testing framework for Solidity contracts.

Version: `v0.1.1`

## Install

If you are using the published package from PyPI:

```bash
pip install solidity-mutate==0.1.1
```

If you want to work on the repository locally:

```bash
git clone https://github.com/sidarth16/solidity-mutate.git
cd solidity-mutate
pip install -e .
```

## Run

Run the tool from the repo root against the bundled Foundry example:

```bash
solidity-mutate examples/test_contract --safe
```

You can also run it as a module:

```bash
python3 -m solidity_mutate examples/test_contract --safe
```

To inspect the available mutators:

```bash
solidity-mutate --list-mutators
```

## CLI Arguments

- `target`
  - Path to the Solidity project root.
  - Default: `.`.
- `--file`
  - Mutate only one Solidity file relative to the project root.
  - Example: `contracts/token.sol`
- `--test-cmd`
  - Command used to run tests for each mutant.
  - Default: `forge test`
- `--mutators`
  - Comma-separated mutators to run.
  - Default: `all`
- `--timeout`
  - Timeout in seconds for each test command run.
  - Default: `30`
- `--safe`
  - Run a preflight test before mutation and a postflight test after mutation.
- `-v`
  - Increase verbosity.
  - Use `-v` for summaries and `-vv` for full mutant logs.
- `--list-mutators`
  - Print the available mutators and exit.

## Repository Layout

- `src/solidity_mutate/`: installable Python package
- `examples/test_contract/`: Foundry sample project used by the mutator
- `pyproject.toml`: package metadata and console script entrypoint

## Sample Project

Run the bundled Foundry example directly:

```bash
cd examples/test_contract
forge test
```

## Sample Results

The bundled example project currently reaches:

- `100%` line coverage
- `100%` statement coverage
- `55.56%` mutation score

### Coverage Report

![Coverage report](https://raw.githubusercontent.com/sidarth16/solidity-mutate/main/assets/coverage.png)

### Mutation Report

![Mutation report](https://raw.githubusercontent.com/sidarth16/solidity-mutate/main/assets/report.png)

### `-vv` Sample Output

![Verbose mutation output](https://raw.githubusercontent.com/sidarth16/solidity-mutate/main/assets/vv.png)

### Full Output

![Full mutation output](https://raw.githubusercontent.com/sidarth16/solidity-mutate/main/assets/output.png)
