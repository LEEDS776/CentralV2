"""
Central AI V2 - Configuration File
"""

class Config:
    # AI Information
    AI_NAME = "Central AI"
    VERSION = "2.0.0"
    DEBUG_MODE = True
    
    # Gemini API Keys - Multiple keys for rotation
    GEMINI_API_KEYS = [
        "AIzaSyDZeiICraGVShpCIhBa2puv7zAFfWsczWM",
        "AIzaSyC3H25B1IeArnerSSma-S67_YaznX-4OkU",
        "AIzaSyBbVFmtBhqk5RgibZmCOJhKFrfi7lBYl34",
        "AIzaSyClG9zuDgjWg0nSq_oAIlG3EHJ2ljfMxuQ",
        "AIzaSyBCT7rfY6Jk4EJRAMmwOJjD0PHapv8FxNU",
        "AIzaSyAKeDucPsOu8pB7k3Q5URZN_dscjrmqE8U",
        "AIzaSyBM6Qoy13ev-mrGQvJd-UxnB7l5aoDwaVA",
        "AIzaSyBcyV7tl1rHtPYQNKiNDEW67dVtB9GlPUo",
        "AIzaSyBS6ewQuHptVRNFw-EzKMmeoltm-m9WDlw",
        "AIzaSyCGytBJOA2hLxlDLu_xS0le-Bg8at3nZQM",
        "AIzaSyDwGtzDnODGRrBtVEGkvL_mpw0Ab5ZHbxI",
        "AIzaSyAmNj84AF5b508UxnIBKAyPU07gIsGrJKE",
        "AIzaSyA0jSFu9T1gsCdRfQB1k3lX81j70XzFXdE",
        "AIzaSyBA5NvGUWPsCdS_g5QtDY3UNpHeMX2hhlw",
        "AIzaSyDPNU9EYAE6QQrnBpKiV0090vtXszTzXVg",
        "AIzaSyB8CsLla9v1zjl_Xj-OMaq5yF-w0mo5_zU",
        "AIzaSyDEOjtMrxK6W9IYRSK6OS2Rh02crKY5638",
        "AIzaSyAzu3H-el6da4vgyy2aEfxu1kPAMkt9ZxY",
        "AIzaSyCt17HJg2KGx8zEoJmlTMZoOSblFKCSFPE",
        "AIzaSyBoE6fnFgoXEbJbJlSG7q6MoHioo20VvcI",
    ]
    
    # Gemini Model Configuration
    GEMINI_MODEL = "gemini-2.0-flash-exp"
    
    # API Settings
    MAX_RETRIES = 3
    TIMEOUT = 30
    
    # Memory Settings
    SHORT_TERM_MEMORY_SIZE = 10
    LONG_TERM_MEMORY_SIZE = 100
    
    # AI Persona - Professional Assistant
    PERSONA = """Kamu adalah Central AI V2, sebuah AI assistant yang powerful dan profesional.

Karakteristik:
- Kamu sangat pintar dalam berbagai bidang: programming, data science, analisis, problem solving
- Kamu memberikan jawaban yang detail, akurat, dan mudah dipahami
- Kamu bisa coding dalam berbagai bahasa pemrograman
- Kamu memiliki memory untuk mengingat konteks percakapan
- Kamu selalu siap membantu dengan ramah dan profesional

Gaya komunikasi:
- Friendly tapi tetap profesional
- Jelaskan konsep complex dengan simple
- Berikan contoh kode yang clean dan well-commented
- Jujur jika tidak tahu sesuatu

Kemampuan khusus:
- Code generation & debugging
- Data analysis & visualization
- Problem solving & algorithm design
- Research & information synthesis
- Creative writing & content creation

Kamu dibuat untuk membantu user secara maksimal dalam berbagai task mereka."""

config = Config()
