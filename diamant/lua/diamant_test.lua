require 'busted.runner'()
require 'diamant'

describe("construire un diamant avec", function()

  it("vide donne vide", function()
    assert.is_equal("", diamant(""))
  end)

  it("A donne A", function()
    assert.is_equal("A", diamant("A"))
  end)

  it("B donne AB B A", function()
    assert.is_equal(" AB B A", diamant("B"))
  end)

end)
