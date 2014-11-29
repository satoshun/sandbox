package main

import (
	"fmt"
	"net/http"
	"regexp"

	"github.com/zenazn/goji"
)

func hello(w http.ResponseWriter, r *http.Request) {
	q := r.URL.Query()["q"]
	fmt.Fprintln(w, "Hello", "World", q)
}

func main() {
	static := regexp.MustCompile("^/(css|js)/")
	goji.Handle(static, http.FileServer(http.Dir("./static")))
	goji.Get("/", hello)
	goji.Serve()
}
