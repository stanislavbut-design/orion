@echo off
for %%f in (STD-001-coding STD-002-database  STD-003-git STD-004-docs STD-005-testing) do type nul > "%%f.md"