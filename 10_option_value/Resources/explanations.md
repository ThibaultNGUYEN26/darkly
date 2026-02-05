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

## Why Does This Happen?

1. **Client-side validation only**: The application relies solely on HTML/JavaScript validation
2. **No server-side checks**: Server accepts any value without verifying it's within valid range
3. **Trust in DOM integrity**: Application assumes users won't modify HTML elements
4. **Missing input validation**: No verification that submitted values match allowed options

## How to Prevent It

1. **Implement server-side validation**: Always validate input on the server, not just client-side
2. **Whitelist valid values**: Check that submitted values are in the list of allowed options
3. **Validate data types and ranges**: Ensure numeric values are within expected bounds
4. **Never trust client data**: Treat all client input as potentially malicious
5. **Use framework validation**: Employ server-side validation frameworks with built-in checks
