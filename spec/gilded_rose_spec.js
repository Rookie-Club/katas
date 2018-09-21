const gildedRoseUpdateQuality = function (name, sellIn, quality) {
  const gildedRose = new Shop([new Item(name, sellIn, quality)]);
  return gildedRose.updateQuality();
}

describe("Gilded Rose shop", function() {

  describe("on the next day", function () {
    it("item name stay 'foo'", function() {
      const items = gildedRoseUpdateQuality("foo", 0, 0);
      expect(items[0].name).toEqual("foo");
    });

    it("item sellIn dont change for Sulfuras, Hand of Ragnaros", function() {
      const items = gildedRoseUpdateQuality('Sulfuras, Hand of Ragnaros', -4, 20);
      expect(items[0].sellIn).toEqual(-4);
    });

    it("item sellIn decrease by one for other item", function() {
      const items = gildedRoseUpdateQuality('+5 Dexterity Vest', 10, 20);
      expect(items[0].sellIn).toEqual(9);
    });

    it("item quality decrease by one for Dexterity vest", function() {
      const items = gildedRoseUpdateQuality('+5 Dexterity Vest', 10, 20);
      expect(items[0].quality).toEqual(19);
    });

    it("item quality decrease twice as fast after sellIn", function() {
      const items = gildedRoseUpdateQuality('+5 Dexterity Vest', 0, 20);
      expect(items[0].quality).toEqual(18);
    });

    it("item quality increase by one for Aged Brie", function() {
      const items = gildedRoseUpdateQuality('Aged Brie', 2, 0);
      expect(items[0].quality).toEqual(1);
    });

    it("item quality never increase more than 50", function() {
      const items = gildedRoseUpdateQuality('Aged Brie', 2, 50);
      expect(items[0].quality).toEqual(50);
    });

    it("item quality never change for Sulfuras, Hand of Ragnaros", function() {
      const items = gildedRoseUpdateQuality('Sulfuras, Hand of Ragnaros', 2, 12);
      expect(items[0].quality).toEqual(12);
    });

    it("item quality stay 0 after sellIn for Backstage passes to a TAFKAL80ETC concert", function() {
      const items = gildedRoseUpdateQuality('Backstage passes to a TAFKAL80ETC concert', 0, 0);
      expect(items[0].quality).toEqual(0);
    });

    it("item quality increase by 3 after sellIn <= 5 for Backstage passes to a TAFKAL80ETC concert", function() {
      const items = gildedRoseUpdateQuality('Backstage passes to a TAFKAL80ETC concert', 5, 10);
      expect(items[0].quality).toEqual(13);
    });

    it("item quality increase by 2 after sellIn <= 10 for Backstage passes to a TAFKAL80ETC concert", function() {
      const items = gildedRoseUpdateQuality('Backstage passes to a TAFKAL80ETC concert', 10, 13);
      expect(items[0].quality).toEqual(15);
    });

    it("item quality increase by 1 after sellIn > 10 for Backstage passes to a TAFKAL80ETC concert", function() {
      const items = gildedRoseUpdateQuality('Backstage passes to a TAFKAL80ETC concert', 11, 16);
      expect(items[0].quality).toEqual(17);
    });

  });


  describe("changeSellIn", function () {
    it("returns a new item with sellIn decreased by one", function () {
      const item = new Item("truc", 3, 5);
      const newItem = decreaseSellIn(item);
      expect(newItem.sellIn).toEqual(2);
    });

    it("Sulfuras, Hand of Ragnaros", function () {
      const item = new Item("Sulfuras, Hand of Ragnaros", 3, 5);
      const newItem = decreaseSellIn(item);
      expect(newItem.sellIn).toEqual(3);
    });
  });


  describe("changeQuality", function () {
    it("returns a new item with quality decreased by one", function () {
      const item = new Item("truc", 3, 5);
      const newItem = changeQuality(item).by(-1);
      expect(newItem.quality).toEqual(4);
    });

    it("returns a new item with quality increased by one", function () {
      const item = new Item("truc", 3, 5);
      const newItem = changeQuality(item).by(+1);
      expect(newItem.quality).toEqual(6);
    });

    it("returns a new item with 0 quality", function () {
      const item = new Item("truc", 3, 5);
      const newItem = changeQuality(item).by(-item.quality);
      expect(newItem.quality).toEqual(0);
    });
  });
});
