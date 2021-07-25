# PyNightmare
PoC for CVE-2021-36934 Aka HiveNightmare/SeriousSAM fully written in python3

# Explanation
CVE-2021-36934 is a recently discovered vulnerability found by @jonasLyk allowing non-admin users to copy all registry hives which contain very private information like hashes which could lead to Privilege Escalation

# Inspiration
Simple Poc for the HiveNightmare vulnerabilty inspired by @GossiTheDog.

# Scope
Works on all versions of Windows 10, where System Protection is enabled.

# What does this PoC do ?
This exploit will look through Volume Shadow Copy to extract registry hives like SAM

#Picture
![image](https://user-images.githubusercontent.com/59793368/126884371-26ff69ba-253c-4507-a481-7daf436bfeae.png)
