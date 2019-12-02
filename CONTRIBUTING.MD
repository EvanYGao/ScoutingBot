# CONTIRBUTING:

### **DO NOT LEAK API KEYS OR URLS**

## STYLE:

1. Use single quotes for strings (when possible). Always use triple double quotes for docstrings. All other multiline strings should
be triple single quoted

2. Use snake_case for variable and function/method names

3. Use reST for docstrings. Seperate param and return statements.

4. Prefer to use single-line comments. Use multi-line comments where > 5 lines. Multi-line comments should be single quoted, as per #1

5. Prefer to use f-strings. If you cannot use f-strings, prefer to use .format before using C-style formatting

6. Use type annotations wherever possible. Use the typing library if necessary in order to do so.

7. Make every command a seperate function. Commands may be split into different files later
