// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.4.26;

import "../contracts/StakeVault.sol";
import "../test/Test.sol";

contract StakeVaultTest is Test {
    function deployStakeVault(address staker, uint64 unlockAt) internal returns (StakeVault) {
        return new StakeVault(staker, unlockAt);
    }

    function testSimpleStake() public {
        StakeVault stakeVault = deployStakeVault(address(456), 100);
        stakeVault.stake(160);
        require(stakeVault.get_staked() == 160, "stake failed");
    }

    function testZeroStake() public {
        StakeVault stakeVault = deployStakeVault(address(456), 100);
        vm.expectRevert(abi.encodeWithSignature("Error(string)", "amount must be > 0"));
        stakeVault.stake(0);
    }

    function testStakeAndWithdrawAfterUnlock() public {
        address staker = address(456);
        StakeVault stakeVault = deployStakeVault(staker, 100);

        require(stakeVault.get_staked() == 0, "init failed");
        require(stakeVault.get_unlock_at() == 100, "unlock time failed");

        stakeVault.stake(250);
        require(stakeVault.get_staked() == 250, "stake failed");

        vm.warp(100);
        vm.prank(staker);
        stakeVault.withdraw(100);

        require(stakeVault.get_staked() == 150, "withdraw failed");
    }

    function testStakeWithdrawTooEarlyShouldFail() public {
        address staker = address(456);
        StakeVault stakeVault = deployStakeVault(staker, 100);

        stakeVault.stake(50);

        vm.warp(99);
        vm.prank(staker);
        vm.expectRevert(abi.encodeWithSignature("Error(string)", "stake is still locked"));
        stakeVault.withdraw(10);
    }
}
