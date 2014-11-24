GRADLE=./gradlew

build: clean
	${GRADLE} build --daemon

clean:
	${GRADLE} clean --daemon

debug:
	${GRADLE} installDebug --daemon

test:
	${GRADLE} connectedAndroidTest --daemon

release: test
	${GRADLE} assembleRelease --daemon
