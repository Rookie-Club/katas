fn fizzbuzz(entree:i32) -> String {
	if entree == 3 {
		return "fizz".to_string()
	} 
	else {
		return entree.to_string()
	}
}


#[test]
fn un_donne_un() {
	assert_eq!("1", fizzbuzz(1));
}
#[test]
fn trois_donne_fizz() {
	assert_eq!("fizz", fizzbuzz(3));
}