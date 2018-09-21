class Poker {

  final static String values = "23456789TJQKA";

  public static String getHighestCard(String card1, String card2) {

    final char card1Value = card1.charAt(0);
    final char card2Value = card2.charAt(0);

    if (values.indexOf(card1Value) >= values.indexOf(card2Value)) {
      return card1;
    }

    return card2;
  }
}
