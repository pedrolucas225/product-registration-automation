# Product Registration Automation

Automated product registration system built with Python. The script reads data from a CSV file and automatically fills in a web-based form, eliminating repetitive manual data entry.

---

## Features

- Automated browser login
- CSV-based data ingestion with Pandas
- Sequential form filling: code, brand, type, category, unit price, cost, and notes
- Graceful handling of optional fields (notes)

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| PyAutoGUI | Keyboard and mouse automation |
| Pandas | Data reading and manipulation |
| python-dotenv | Secure credential management |

---

## Getting Started

### Prerequisites

- Python 3.12+
- Google Chrome installed

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/pedrolucas225/automacao-cadastro-de-produtos.git
cd automacao-cadastro-de-produtos
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**

Create a `.env` file in the project root:
```env
EMAIL=your-email@example.com
PASSWORD=your-password
```

**4. Add your data file**

Place a `produtos.csv` file in the project root with the following columns:

| Column | Description |
|--------|-------------|
| `codigo` | Product code |
| `marca` | Brand |
| `tipo` | Type |
| `categoria` | Category |
| `preco_unitario` | Unit price |
| `custo` | Cost |
| `obs` | Notes (optional) |

**5. Run the script**
```bash
python codigo.py
```

---

## Project Structure

```
automacao-cadastro-de-produtos/
├── codigo.py           # Main automation script
├── requirements.txt    # Project dependencies
├── .gitignore
├── .env                # Secret credentials (not versioned)
└── produtos.csv        # Input data (not versioned)
```

---

## Security

Credentials are stored in a `.env` file which is excluded from version control via `.gitignore`. Never commit or share this file.

---

## Author
