import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class HigherValueShould {
  @Disabled
  @Test
  void a_valid_hand_has_exactly_five_cards() {
  }

  @Test
  void returns_3D_because_its_higher_than_2H() {
    assertThat(Poker.getHighestCard("2H", "3D"))
        .isEqualTo("3D");
  }

  @Test
  void returns_4E_because_its_higher_than_3H() {
    assertThat(Poker.getHighestCard("4D", "3H"))
        .isEqualTo("4D");
  }

  @Test
  void returns_JD_because_its_higher_than_TH() {
    assertThat(Poker.getHighestCard("TH", "JD"))
        .isEqualTo("JD");
  }
}