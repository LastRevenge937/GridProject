from core.firewall import Firewall

# ... inside main() after config and before booting layers

# Ask user if they want a custom firewall
use_custom_fw = input("Do you want to attach a custom global firewall? (y/n): ").strip().lower()
if use_custom_fw == "y":
    fw_name = input("Enter firewall name: ").strip()
    # Here you could extend to accept a subclass of Firewall if implemented
    custom_fw = Firewall(fw_name)
else:
    custom_fw = Firewall("Castle Default Firewall")

grid.attach_global_firewall(custom_fw)
