#######################################################################################################################
### The message
"""The Report for Account OCP contains 5,000 Transactions with 1.45 Bil revenue"""

### one of the old ways
"""The Report for Account %s contains %d Transactions with %1.2f Bil revenue""" % ("OCP", 5000, 1.45)

### The new ways
"""The Report for Account {} contains {} Transactions with {:1.2f} Bil revenue""".format("OCP", 5000, 1.45)

"""The Report for Account {1} contains {2} Transactions with {0:1.2f} Bil revenue""".format(1.45, "OCP", 5000)

"""The Report for Account {acc} contains {trans} Transactions with {rev:1.2f} Bil revenue""".format(rev=1.45, acc="OCP", trans=5000)

var_tuple = ("OCP", 5000, 1.45)
"""The Report for Account {} contains {} Transactions with {:1.2f} Bil revenue""".format(*var_tuple)

var_dict = {"rev": 1.45, "acc": "OCP", "trans": 5000}
"""The Report for Account {acc} contains {trans} Transactions with {rev:1.2f} Bil revenue""".format(**var_dict)


### Starting with version 3.6

acc = "OCP"
trans = 5000
rev = 1.45
f"""The Report for Account {acc} contains {trans} Transactions with {rev:1.2f} Bil revenue"""

# or very freestyle
f"""The Report for Account {var_dict['acc']} contains {trans*5000/5000} Transactions with {var_tuple[2]:1.2f} Bil revenue"""




