<h1>Algorithm for updating access files through Python</h1>

 ### You can also read this in: [Português](https://github.com/GLMello/Alg-Updt-Pyth)

<h2>Description</h2>
Developing an algorithm responsible for updating a file containing IPs allowed to a network by checking their access and removing banned addresses from it.<br>  <br />

**Note:**  In order to better visualize the code, fictional IPs and an examplary file were used. Later in development, the presented IPs are substituted for a file to allow scalability.<br>
<h2>Walk-through</h2>
I began by developing a short code that opened the original file and displayed its contents, along with inserting a fictional banned ip list:
 <br/>

```python
# Assigning variable to the name of the file.

import_file = "allow_list.txt"

# List of IP addresses that are no longer allowed to access restricted information. 

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:

  # Read and stores the imported file to a variable as a string.

  ip_addresses=file.read()

print(ip_addresses) 
```
 <br/>
I then added the following lines in order to convert the contents to a list, iterate through the 'remove list' and remove the matching IP addresses from the contents:  
  <br/>

```python
# Converts the contents from a string to a list

ip_addresses = ip_addresses.split()

# Loops through `remove_list`, looks for matches and removes them from the list.

for element in remove_list:
    if element in ip_addresses: 
        ip_addresses.remove(element)
```
<br />
Converting the list back to a string and updating allow us to update the original file:
<br />

```python
# Converts the list back to a string.

ip_addresses = "\n".join(ip_addresses)

# Rewrite the file, replacing its contents with `ip_addresses`

with open(import_file, "w") as file:
  file.write(ip_addresses)
```
<br />
To finish it off, I made the code into a function which takes in two files as parameters, one containing a list of authorized IPs and one containing banned IP addresses. Ending up with the completed algorithm:
  <br/>
  
  ```python

def update_file(import_file, remove_file):

# Assigns variables to take in the files contents.

    with open(import_file, "r") as allow_file:
        ip_addresses = allow_file.read()
    
    with open(remove_file, "r") as remove_list: 
        remove_list = remove_file.read()

# Converts the contents from a string to a list.

    remove_list = remove_list.split()

    ip_addresses = ip_addresses.split()

# Loops through `remove_list`, looks for matches and removes them from the list.

    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)

# Converts the list back to a string.

    ip_addresses = "\n".join(ip_addresses)

# Rewrite the file, replacing its contents with the list's.
    with open(import_file, "w") as allow_file:
        allow_file.write(ip_addresses)

```

