// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.4.26;

contract Vault {
    address public owner;
    uint256 private balance_;

    constructor(address _owner) public {
        owner = _owner;
    }

    function deposit(uint256 amount) external {
        require(amount > 0, "amount must be > 0");
        balance_ += amount;
    }

    function withdraw(uint256 amount) external {
        require(msg.sender == owner, "only owner");
        require(balance_ >= amount, "insufficient balance");
        balance_ -= amount;
    }

    function get_balance() external view returns (uint256) {
        return balance_;
    }
}
