"""
Language Translation Tool
CodeAlpha AI Internship - Task 1

Features:
- Translate text between 26+ languages
- Auto detect source language
- Uses Google Translate API (googletrans library)
- Simple terminal interface
"""

from googletrans import Translator, LANGUAGES

# ══════════════════════════════════════════════
# INITIALIZE TRANSLATOR
# ══════════════════════════════════════════════
translator = Translator()

# ══════════════════════════════════════════════
# SUPPORTED LANGUAGES
# ══════════════════════════════════════════════
SUPPORTED_LANGUAGES = {
    "1":  ("en", "English"),
    "2":  ("ur", "Urdu"),
    "3":  ("ar", "Arabic"),
    "4":  ("hi", "Hindi"),
    "5":  ("fr", "French"),
    "6":  ("de", "German"),
    "7":  ("es", "Spanish"),
    "8":  ("it", "Italian"),
    "9":  ("pt", "Portuguese"),
    "10": ("ru", "Russian"),
    "11": ("zh-cn", "Chinese (Simplified)"),
    "12": ("ja", "Japanese"),
    "13": ("ko", "Korean"),
    "14": ("tr", "Turkish"),
    "15": ("nl", "Dutch"),
    "16": ("pl", "Polish"),
    "17": ("sv", "Swedish"),
    "18": ("id", "Indonesian"),
    "19": ("ms", "Malay"),
    "20": ("th", "Thai"),
    "21": ("vi", "Vietnamese"),
    "22": ("fa", "Persian"),
    "23": ("he", "Hebrew"),
    "24": ("uk", "Ukrainian"),
    "25": ("bn", "Bengali"),
    "26": ("auto", "Auto Detect"),
}

# ══════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════
def show_languages():
    """Display all supported languages"""
    print("\n" + "=" * 50)
    print("         SUPPORTED LANGUAGES")
    print("=" * 50)
    for num, (code, name) in SUPPORTED_LANGUAGES.items():
        print(f"  {num:>2}. {name} ({code})")
    print("=" * 50)

def get_language_choice(prompt, exclude_auto=False):
    """Get language selection from user"""
    show_languages()
    while True:
        choice = input(prompt).strip()
        if choice in SUPPORTED_LANGUAGES:
            code, name = SUPPORTED_LANGUAGES[choice]
            if exclude_auto and code == "auto":
                print("  ❌ Auto detect not available for target language. Try again.")
                continue
            return code, name
        print("  ❌ Invalid choice. Please enter a number from the list.")

def translate_text(text, src_lang, tgt_lang):
    """
    Translate text using Google Translate API
    Args:
        text: Text to translate
        src_lang: Source language code
        tgt_lang: Target language code
    Returns:
        Translated text and detected language
    """
    try:
        if src_lang == "auto":
            result = translator.translate(text, dest=tgt_lang)
        else:
            result = translator.translate(text, src=src_lang, dest=tgt_lang)
        return result.text, result.src
    except Exception as e:
        return None, str(e)

def detect_language(text):
    """Detect the language of input text"""
    try:
        detected = translator.detect(text)
        lang_name = LANGUAGES.get(detected.lang, detected.lang)
        return lang_name, detected.confidence
    except:
        return "Unknown", 0

# ══════════════════════════════════════════════
# MAIN TRANSLATION TOOL
# ══════════════════════════════════════════════
def run_translator():
    print("=" * 60)
    print("      Language Translation Tool")
    print("      CodeAlpha AI Internship - Task 1")
    print("      Powered by Google Translate API")
    print("=" * 60)
    print("\nWelcome to the Language Translation Tool!")
    print("Translate text between 26+ languages instantly.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        print("\n" + "-" * 60)
        print("OPTIONS:")
        print("  1. Translate text")
        print("  2. Detect language")
        print("  3. Show all languages")
        print("  4. Exit")
        print("-" * 60)

        choice = input("Enter your choice (1-4): ").strip()

        # ── TRANSLATE ──
        if choice == "1":
            print("\n📝 Enter text to translate (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            text = " ".join(lines).strip()

            if not text:
                print("❌ No text entered. Please try again.")
                continue

            # Source language
            print("\nSelect SOURCE language:")
            src_code, src_name = get_language_choice(
                "Enter source language number (choose 26 for Auto Detect): "
            )

            # Target language
            print("\nSelect TARGET language:")
            tgt_code, tgt_name = get_language_choice(
                "Enter target language number: ",
                exclude_auto=True
            )

            print("\n⏳ Translating...")
            translated, detected_src = translate_text(text, src_code, tgt_code)

            if translated:
                print("\n" + "=" * 60)
                print("✅ TRANSLATION RESULT")
                print("=" * 60)
                print(f"📌 Original Text  : {text}")
                if src_code == "auto":
                    detected_name = LANGUAGES.get(detected_src, detected_src)
                    print(f"🔍 Detected Language: {detected_name.title()}")
                print(f"🌍 Target Language : {tgt_name}")
                print(f"📝 Translation     : {translated}")
                print("=" * 60)

                # Copy option
                copy = input("\nDo you want to translate another text? (yes/no): ").strip().lower()
                if copy not in ["yes", "y"]:
                    print("\n✅ Thank you for using the Translation Tool!")
                    break

            else:
                print(f"\n❌ Translation failed: {detected_src}")
                print("Please check your internet connection and try again.")

        # ── DETECT LANGUAGE ──
        elif choice == "2":
            text = input("\n📝 Enter text to detect language: ").strip()
            if not text:
                print("❌ No text entered.")
                continue
            print("\n⏳ Detecting language...")
            lang_name, confidence = detect_language(text)
            print(f"\n✅ Detected Language: {lang_name.title()}")
            print(f"   Confidence: {round(confidence * 100)}%")

        # ── SHOW LANGUAGES ──
        elif choice == "3":
            show_languages()

        # ── EXIT ──
        elif choice in ["4", "quit", "exit"]:
            print("\n👋 Goodbye! Thank you for using the Translation Tool!")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    run_translator()
