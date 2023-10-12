[中文说明](README_zh.md) 

## How To Use
![](/Others/Q9RVLdhun7.png)
- Double click [main.bat](main.bat)
- Select folder
- Click export button

> First time use and setup:
> - Click [setup.bat](setup.bat) will automatically call python installer(check on Add Python 3.10 to PATH)
> - Click [setup_dependence.bat](setup_dependence.bat) will automatically install dependency

## Config Rule
There are some showcase at [Example](Example) folder
- proto description: https://developers.google.com/protocol-buffers/docs/proto3
- excel description:
    - First row is description, Second row is parameter name, Third and blow is config data
    - Support one Sheet
    - Use,split array

## Export Data
![](/Others/FvCsQi9QOz.png)
- json (check exported data easily)
- bin (binary data)
- pb (description data)

## Export Language
- cpp
- csharp
- java
- python

-----

## More:

### Convert Rule
standard python data types: 
https://docs.python.org/3/library/stdtypes.html#

google official convert rule: https://developers.google.com/protocol-buffers/docs/proto3
![](/Others/vbBuHG4DUC.png)

Convert rule:
- int32,sint32,sfixed32 to int

- double,float to float

- int64,uint32,uint64,sint64,fixed32,fixed64,sfixed64 to int(not long)

- bool to bool

- string to str

- bytes to bytes

why convert int64,uint32.etc to int? because in python 3.x only one default integer value type int:

>PEP 237: Essentially, long renamed to int. That is, there is only one built-in integral type, named int; but it behaves mostly like the old long type.https://docs.python.org/3/whatsnew/3.0.html#integers

### Log
- Write into logs folder
- Search "Error" in log files find export problems


-----

## Develop

### Python Style Guide
https://google.github.io/styleguide/pyguide.html

### Language Extend 

#### Official Support Language 
- Only export common/no library dependence language
- go, dart .etc language need tools or library to export, can extend those language by self 

#### Other Language Support 
- Lua
  - There are description file .pb, data file .bin, many open source can deserialize to lua table(Most common use)
  - There are .json file with data and format, many open source can transform json to lua file
  - Lua in Unreal Engine/Unity Engine mostly use .pb and .bin 

support: hiramtan@live.com