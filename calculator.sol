// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract calc {

    uint256 res = 0;

    function add(uint256 num) public {
        res += num;
    }

    function sub(uint256 num) public {
       res -= num;
    }

    function mul(uint256 num) public {
        res *= num;
    }

    function sqrt_floor() public { //the integer just less than or equal to square root of the num
        uint256 i = 1;
        while(i*i <= res) i++;
        res = i - 1;
    }

    function raise_pwr(uint256 num) public {
        uint256 temp = res;
        for(uint256 i = 1; i < num; i++) {
            res *= temp;
        }
    }

    function get_res() public view returns (uint256) {
        return res;
    }
}
