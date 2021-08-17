package main

import "fmt"

func main() {

	firstName := "Chigozie"
	lastName := "Nwokoye"
	func(firstName string, lastName string) {
		fullName := lastName + " " + firstName
		fmt.Println(fullName)
	}(firstName, lastName)

}
