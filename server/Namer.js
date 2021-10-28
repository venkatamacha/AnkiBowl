class Namer {

    constructor() {

        // TODO: customize this by category
        this.names = [
            "Alligator",
            "Armadillo",
            "Auroch",
            "Axolotl",
            "Badger",
            "Bat",
            "Bear",
            "Beaver",
            "Buffalo",
            "Camel",
            "Capybara",
            "Chameleon",
            "Cheetah",
            "Chinchilla",
            "Chipmunk",
            "Chupacabra",
            "Cormorant",
            "Coyote",
            "Crow",
            "Dinosaur",
            "Dolphin",
            "Duck",
            "Elephant",
            "Ferret",
            "Fox",
            "Frog",
            "Giraffe",
            "Gopher",
            "Grizzly",
            "Hedgehog",
            "Hippo",
            "Ibex",
            "Ifrit",
            "Iguana",
            "Jackal",
            "Kangaroo",
            "Koala",
            "Kraken",
            "Lemur",
            "Leopard",
            "Liger",
            "Lion",
            "Llama",
            "Loris",
            "Manatee",
            "Mink",
            "Monkey",
            "Moose",
            "Narwhal",
            "Nyan Cat",
            "Orangutan",
            "Otter",
            "Panda",
            "Penguin",
            "Platypus",
            "Pumpkin",
            "Python",
            "Quagga",
            "Rabbit",
            "Raccoon",
            "Rhino",
            "Sheep",
            "Shrew",
            "Squirrel",
            "Tiger",
            "Turtle",
            "Walrus",
            "Wolf",
            "Wolverine",
            "Wombat"      
        ];
        
    }

    random() {
        return this.names[Math.floor(Math.random() * this.names.length)];
    }

}

module.exports = new Namer();