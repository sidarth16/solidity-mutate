// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.4.26;

interface Vm {
    function prank(address newMsgSender) external;
    function warp(uint256 newTimestamp) external;
    function expectRevert(bytes revertData) external;
}

contract Test {
    Vm internal vm;

    constructor() public {
        vm = Vm(address(uint160(uint256(keccak256("hevm cheat code")))));
    }
}
