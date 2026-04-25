// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.4.26;

contract StakeVault {
    address public staker;
    uint256 private staked_;
    uint64 private unlockAt_;

    constructor(address _staker, uint64 _unlockAt) public {
        staker = _staker;
        unlockAt_ = _unlockAt;
    }

    function stake(uint256 amount) external {
        require(amount > 0, "amount must be > 0");
        staked_ += amount;
    }

    function withdraw(uint256 amount) external {
        require(msg.sender == staker, "only staker");
        require(block.timestamp >= unlockAt_, "stake is still locked");
        require(staked_ >= amount, "insufficient stake");
        staked_ -= amount;
    }

    function get_staked() external view returns (uint256) {
        return staked_;
    }

    function get_unlock_at() external view returns (uint64) {
        return unlockAt_;
    }
}
