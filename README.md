
L'idée d'une expression régulière est de retrouver un motif dans une chaîne de caractères

les tests pourrait être :
```python
mafonction("une chaine de caractères totalement banale", "z") => False
mafonction("une chaine de caractères totalement banale", "[0-9]") => False
mafonction("une chaine de caractères totalement banale", "banale") => True
mafonction("une chaine de caractères totalement banale", "[a-zA-Z]") => True
```