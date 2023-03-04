document.addEventListener("DOMContentLoaded", function(event) { 
    document.getElementById("uploadSongUrl").addEventListener("submit", (e) => {
        e.preventDefault();

        var songUrl = document.getElementById("song_url").value;

        var found = false;

        var xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status==200) {
                document.getElementById("loader").classList.add("hiddenToggle");
                res = JSON.parse(xhr.responseText);

                document.getElementById("song_name").innerHTML = res['song_name'];
                document.getElementById("song_lyrics").innerHTML = res['song_lyrics'];
                document.getElementById("song_meaning").innerHTML = res['song_meaning'].replace("\\n","<br>");

                document.getElementById("songInfo").classList.remove("hiddenToggle");
                document.getElementById("progress").value = 0;
                found = true;
            } else if (xhr.readyState == 4) {
                alert("Failed");
                found = true;
            }
        };

        nid = Math.floor(Math.random()*100000) + 1

        xhr.open("POST", "/upload");
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        document.getElementById("loader").classList.remove("hiddenToggle");
        xhr.send(`song_url=${songUrl}&nid=${nid}`);

        function checkProgress() {
            fetch("/progress/" + nid).then(data => data.text())
            .then((data) => {
                document.getElementById("progress").value = parseInt(data);
                if (!found) {
                    setTimeout(checkProgress, 2000);
                }
            });
        }
        setTimeout(checkProgress,1000);
    });
});