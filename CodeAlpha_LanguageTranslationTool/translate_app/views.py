

from django.shortcuts import render
from deep_translator import GoogleTranslator, MyMemoryTranslator


def translate_text(text, source, target):
    # Pehle Google try karo
    try:
        return GoogleTranslator(source=source, target=target).translate(text)
    except Exception:
        pass

    # Google fail hua toh MyMemory try karo
    if source == "auto":
        return "Google abhi busy hai. Please 'From' mein language manually select karo."
    try:
        return MyMemoryTranslator(source=source, target=target).translate(text)
    except Exception as e:
        return f"Translation failed: {e}"


def translate_view(request):
    languages = GoogleTranslator().get_supported_languages()  # list of names
    translated = ""
    text = ""
    source = "auto"
    target = "english"

    if request.method == "POST":
        text = request.POST.get("text", "")
        source = request.POST.get("source", "auto")
        target = request.POST.get("target", "english")
        if text.strip():
            translated = translate_text(text, source, target)

    return render(request, "translate_app/translate.html", {
        "languages": languages,
        "translated": translated,
        "text": text,
        "source": source,
        "target": target,
    })