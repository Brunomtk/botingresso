
---

## 🎟️ Verificador de Ingressos — **ARQ Automático**

> Monitore a página do seu evento e receba alerta sonoro assim que os ingressos forem liberados!

---

### 🧠 O que é?

Esse script Python abre o navegador automaticamente, fica monitorando a página do evento e **toca um áudio personalizado** assim que os ingressos estiverem disponíveis. Tudo isso enquanto você vive sua vida tranquilo.

---

### 🚀 Como usar

#### 1. Clone ou baixe este projeto

```bash
git clone https://github.com/seuusuario/verificador-ingressos-arq.git
```

Ou simplesmente coloque o arquivo `arq.py` em uma pasta local.

---

#### 2. Instale os requisitos

Abra o terminal (cmd, PowerShell ou VSCode) e instale os pacotes necessários:

```bash
pip install selenium pygame chromedriver-autoinstaller
```

---

#### 3. Ajuste o caminho do áudio

Na linha 10 do `arq.py`, altere para o caminho do seu áudio `.mp3` ou `.wav`:

```python
audio = r"C:\Users\bruno\Downloads\arq\arq\audio\meu_audio.mp3"
```

> Dica: use **`r""`** para evitar erros com `\`.

---

#### 4. Execute o script

```bash
python arq.py
```

Ele vai abrir o site do evento e começar a monitorar.

---

### 🔁 O que ele faz?

* Abre o site do evento no navegador (com Chrome)
* Fica verificando se os ingressos foram liberados
* Quando encontra, toca seu áudio de aviso (ex: funkão, grito, alerta)
* Abre a página no navegador para você comprar
* Encerra sozinho após o alerta

---

### 🛠️ Requisitos

* Python 3.10+ (compatível com 3.12)
* Google Chrome instalado
* ChromeDriver (instalado automaticamente via `chromedriver-autoinstaller`)

---

### 📁 Estrutura sugerida da pasta

```
arq/
│
├── arq.py
├── README.md
└── audio/
    └── alerta.mp3
```

---

### 🤖 Personalização

Quer deixar mais a sua cara?

* Troque o som por algo engraçado, romântico ou explosivo 💥
* Mude o site do evento para qualquer outro, desde que o botão tenha uma classe HTML identificável

---

### ⚠️ Atenção

* O site precisa **manter o botão de compra visível** com a classe `ingresso-quantidade` para funcionar corretamente.
* O script não faz compra automática. Ele apenas **avisa você imediatamente**.

---

### ❤️ Autor

Feito com carinho por um fã de eventos que não quer perder mais ingressos.
Te cuida que agora você vai ser o primeiro da fila.

---

