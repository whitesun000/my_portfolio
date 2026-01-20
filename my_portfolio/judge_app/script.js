function startListen(targetId) {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'ja-JP';

    recognition.onstart = () => {
        document.getElementById(targetId).style.backgroundColor = "#fff9cd";
    };

    recognition.onresult = (event) => {
        let transcript = event.results[0][0].transcript;
        let number = transcript.replace(/[^0-9]/g, "");
        if (number) {
            document.getElementById(targetId).value = number;
        }
    };

    recognition.onend = () => {
        document.getElementById(targetId).style.backgroundColor = "";
    };

    recognition.start();
}