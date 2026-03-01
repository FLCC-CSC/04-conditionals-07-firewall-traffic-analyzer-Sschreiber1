# FILE NAME - firewall_traffic_analyzer.py

# NAME: Steven Schreiber
# DATE: 2/27/2026
# BRIEF DESCRIPTION: Creating a firewall trafic analyzer. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

########################################
def assess_risk(port, size_mb):
    # Port 22 and 3389 are always HIGH RISK
    if port == 22 or port == 3389:
        return "HIGH RISK: Potential unauthorized remote access detected!"

    # Port 80 logic
    if port == 80:
        if size_mb > 100:
            return "MEDIUM RISK: Large unencrypted data transfer detected."
        else:
            return "UNKNOWN: Unrecognized traffic pattern."

    # Port 443 is always LOW RISK
    if port == 443:
        return "LOW RISK: Secure encrypted transfer detected."

    # All other ports
    return "UNKNOWN: Unrecognized traffic pattern."


def run_analyzer():
    print("=== Network Traffic Security Analyzer ===")
    port = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
    size_mb = int(input("Enter the data transfer size in megabytes (MB): "))

    risk = assess_risk(port, size_mb)

    print(f"Risk Assessment: {risk}")

########################################

########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 12

FIREWALL LOG:
Port: 22, Transfer Size: 12 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?
I had to be careful when using "or" and "and" because they mean different things. "and" requires both conditions to be true, while "or" only needs one






'''
