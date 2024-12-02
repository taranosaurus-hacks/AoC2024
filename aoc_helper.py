import dotenv
import os
from pathlib import Path
import requests

class AdventOfCode:
    def __init__(self, year:int, day:int) -> None:
        dotenv.load_dotenv()
        self.AOC_SESSION = os.getenv("AOC_SESSION")
        self.year = year
        self.day = day
        self.input_dir = "inputs"
        self.input_file = f"{year}_{day}.input"
        self.input_path = os.path.join(self.input_dir, self.input_file)
    
    def _check_input(self):
        if Path(self.input_path).is_file():
            print(f"Opening {self.input_path}")
            with open(self.input_path) as f:
                input_data = f.read().strip()
                return input_data
        else:
            return False
    
    def _save_input(self, input_data):
        with open(self.input_path, "w+", encoding="utf-8") as f:
            f.write(input_data)
            print(f"Saved {self.input_path}")
    
    def get_input(self):
        input_data = self._check_input()
        if not input_data:
            response = requests.get(url=f"https://adventofcode.com/{self.year}/day/{self.day}/input", headers={"Cookie": f"session={self.AOC_SESSION}"})
            if response.status_code == 200:
                input_data = response.text.strip()
                self._save_input(input_data=response.text)
            else:
                print(f"Error: {response.text}")
                exit(1)
        return input_data