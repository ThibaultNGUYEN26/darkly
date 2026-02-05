# Option Value Manipulation Vulnerability

## Discovery Process

1. Navigate to the survey page
2. Notice that grade values appear to be restricted
3. Inspect the HTML form using browser developer tools
4. Identify that grades are defined in `<option>` elements with fixed values

## Vulnerability Details

- **Issue**: Client-side validation relies on HTML option values
- **Attack vector**: Manipulating option values in the DOM before submission
- **Weakness**: No server-side validation of input ranges

## Exploitation

1. Open browser developer tools (F12) and inspect the grade dropdown
2. Locate the option element:
```html
<option value="2">2</option>
```
3. Modify the value attribute to an invalid value:
```html
<option value="42">2</option>
```
4. Select the modified grade option
5. Submit the form
6. Successfully obtained the flag
