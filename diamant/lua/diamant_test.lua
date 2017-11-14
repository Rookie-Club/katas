require 'busted.runner'()
require 'diamant'

describe("construire un diamant avec", function()

  it("vide donne vide", function()
    assert.is_equal("", diamant(""))
  end)

  it("A donne A", function()
    assert.is_equal("A", diamant("A"))
  end)

  it("B donne  A \
              B B\
               A", function()
    assert.is_equal(" A\nB B\n A", diamant("B"))
  end)

  it("C donne  A\
              B B\
             C   C\
              B B\
               A", function()
    assert.is_equal("  A\n B B\nC   C\n B B\n  A", diamant("C"))
  end)

end)
