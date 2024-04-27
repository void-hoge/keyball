getarray: dancing_cat.mp4
	./video2binary.py dancing_cat.mp4

dancing_cat.mp4:
	mpv --stream-record=dancing_cat.mkv 'https://youtu.be/D1xvBOsy5vk?si=ckGVJTH2LOXMSMuO' --volume=20
	ffmpeg -i dancing_cat.mkv -map 0 -c copy -c:a aac dancing_cat.mp4

clean:
	rm *.mkv *.mp4
