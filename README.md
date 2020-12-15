# XSScanner
Basic Automatic XSS Scanner 

# Resources
- [Usage](#Usage)
- [Installation](#Installation)

 # Usage

```python
python3 ScannerXSS.py Urls.txt '"><svg/onload=prompt(1)>'
```

# Examples

## Urls.txt

```
https://www.XXX.com/search/?q=tester&id=valuetest
http://XXX.free/XX/XX/recherche.php?motclef=simple
https://XX.com/XXX?n=aporlorxl23&Other=Aporlox
https://XXX.XXX.com/?for=bing.com
```


 # Installation

### From Github

```sh
git clone https://github.com/Aporlorxl23/XSScanner.git
python3 ScannerXSS.py Urls.txt '"><svg/onload=prompt(1)>'
```
