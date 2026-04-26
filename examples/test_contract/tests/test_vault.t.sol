// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.4.26;

import "../contracts/Vault.sol";
import "../test/Test.sol";

contract VaultTest is Test {
    function deployVault(address owner) internal returns (Vault) {
        return new Vault(owner);
    }

    function testSimpleDeposit() public {
        Vault vault = deployVault(address(123));
        vault.deposit(100);
        require(vault.get_balance() == 100, "deposit failed");
    }

    function testVaultZeroDepositShouldFail() public {
        Vault vault = deployVault(address(123));
        vm.expectRevert(abi.encodeWithSignature("Error(string)", "amount must be > 0"));
        vault.deposit(0);
    }

    function testVaultDepositAndOwnerWithdraw() public {
        address owner = address(123);
        Vault vault = deployVault(owner);

        require(vault.get_balance() == 0, "init failed");

        vault.deposit(100);
        require(vault.get_balance() == 100, "deposit failed");

        vm.prank(owner);
        vault.withdraw(40);
    }
}
