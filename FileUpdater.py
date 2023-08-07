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

# Rewrite the file, replacing its contents with `ip_addresses`

  with open(import_file, "w") as allow_file:
      allow_file.write(ip_addresses)