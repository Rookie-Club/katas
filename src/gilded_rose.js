class Item {
  constructor(name, sellIn, quality){
    this.name = name;
    this.sellIn = sellIn;
    this.quality = quality;
  }
}
/*
const Item = (name, sellIn, quality) => {
  return {name, sellIn, quality};
}
*/

const changeQuality = (item) => {
  return {
    by: (quality) => {
      return new Item(item.name, item.sellIn, item.quality + quality);
    }
  }
}

const decreaseSellIn = (item) => {
  if (item.name == "Sulfuras, Hand of Ragnaros") {
    return item;
  } else {
    return new Item(item.name, item.sellIn - 1, item.quality);
  }
}

class Shop {
  constructor(items=[]){
    this.items = items;
  }
  updateQuality() {
    for (var i = 0; i < this.items.length; i++) {
      if (this.items[i].name != 'Aged Brie' && this.items[i].name != 'Backstage passes to a TAFKAL80ETC concert') {
        if (this.items[i].quality > 0) {
          if (this.items[i].name != 'Sulfuras, Hand of Ragnaros') {
            this.items[i] = changeQuality(this.items[i]).by(-1);
          }
        }
      } else {
        if (this.items[i].quality < 50) {
          this.items[i] = changeQuality(this.items[i]).by(+1);
          if (this.items[i].name == 'Backstage passes to a TAFKAL80ETC concert') {
            if (this.items[i].sellIn < 11) {
              if (this.items[i].quality < 50) {
                this.items[i] = changeQuality(this.items[i]).by(+1);
              }
            }
            if (this.items[i].sellIn < 6) {
              if (this.items[i].quality < 50) {
                this.items[i] = changeQuality(this.items[i]).by(+1);
              }
            }
          }
        }
      }
      this.items[i] = decreaseSellIn(this.items[i]);
      if (this.items[i].sellIn < 0) {
        if (this.items[i].name != 'Aged Brie') {
          if (this.items[i].name != 'Backstage passes to a TAFKAL80ETC concert') {
            if (this.items[i].quality > 0) {
              if (this.items[i].name != 'Sulfuras, Hand of Ragnaros') {
                this.items[i] = changeQuality(this.items[i]).by(-1);
              }
            }
          } else {
            this.items[i] = changeQuality(this.items[i]).by(-this.items[i].quality);
          }
        } else {
          if (this.items[i].quality < 50) {
            this.items[i] = changeQuality(this.items[i]).by(+1);
          }
        }
      }
    }

    return this.items;
  }
}
