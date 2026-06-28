import subprocess
import re

# ---------------- PASSWORD CHECK ---------------- #
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&*!]", password):
        score += 1

    if score <= 2:
        return "Weak ❌"
    elif score <= 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"


# ---------------- GET WIFI PASSWORDS ---------------- #
def get_wifi_profiles():
    command = "netsh wlan show profiles"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    profiles = re.findall("All User Profile\s*:\s(.*)", result.stdout)
    return profiles


def get_wifi_password(profile):
    command = f'netsh wlan show profile "{profile}" key=clear'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    match = re.search("Key Content\s*:\s(.*)", result.stdout)
    return match.group(1) if match else None


# ---------------- MAIN ---------------- #
def wifi_audit():
    print("\n🔍 WiFi Security Audit\n")

    profiles = get_wifi_profiles()

    for profile in profiles:
        password = get_wifi_password(profile)

        if password:
            strength = check_strength(password)
            print(f"WiFi: {profile}")
            print(f"Password: {password}")
            print(f"Strength: {strength}")
            print("-" * 40)
        else:
            print(f"WiFi: {profile} (No password found)")
            print("-" * 40)


if __name__ == "__main__":
    wifi_audit()