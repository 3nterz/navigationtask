# Global configuration file

# File:   config.py
# Author: Nathan Tarr

# General Town Scenery Setup
unitScale = 5.0
wallHeight = 2.0
curbHeight = 0.2

blackImage = Image("scenery/black.png")
whiteImage = Image("scenery/white.png")

wallImage = Image("scenery/wall.png")
wallImagelen=0.5
skyImage = Image("scenery/sky.png")
groundImage = Image("scenery/sidewalk2.png")
groundImageLen = 4.0
curbImage = Image("scenery/curb.png")
sidewalkImage = Image("scenery/sidewalk.png")
sidewalkTexLen = 6.0

# Guided Camera Setup
camHeight = min(2.0, wallHeight)
camFOV = 60.0

# Avatar Control Information
eyeFOV = 60.0
eyeHeight = min(2.0, wallHeight)
avatarRadius = 0.5
fullForwardSpeed = 0.005 # VR Units / millisecond
fullBackwardSpeed = 0.005
maximumLinearAcceleration = 0.000008
fullTurnSpeed = 0.0005 # radians / milliseconds
forwardButton = Key("UP")
backwardButton = Key("DOWN")
leftButton = Key("LEFT")
rightButton = Key("RIGHT")

# Landmark definitions
labelledA = Pool(
	PoolDict(
		name = "Burger City",
		image = Image("LandmarksGroupA/labelled/burger_city.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Candle Shop",
		image = Image("LandmarksGroupA/labelled/candle_shop.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Cookie Shop",
		image = Image("LandmarksGroupA/labelled/cookie_shop.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Family Place",
		image = Image("LandmarksGroupA/labelled/family_place.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Food Market",
		image = Image("LandmarksGroupA/labelled/food_market.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Golden Palace",
		image = Image("LandmarksGroupA/labelled/golden_palace.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "House of Pizza",
		image = Image("LandmarksGroupA/labelled/house_pizza.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Mike's Restaurant",
		image = Image("LandmarksGroupA/labelled/mikes_restaurant.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Pet Care Center",
		image = Image("LandmarksGroupA/labelled/pet_care_center.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "The Piano Store",
		image = Image("LandmarksGroupA/labelled/piano_store.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	)
)

# Landmark definitions
labelledB = Pool(
	PoolDict(
		name = "Butcher Shop",
		image = Image("LandmarksGroupB/labelled/butcher_shop.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Costume Party",
		image = Image("LandmarksGroupB/labelled/costume_party.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "The Coffee Store",
		image = Image("LandmarksGroupB/labelled/coffee_store.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Flower Patch",
		image = Image("LandmarksGroupB/labelled/flower_patch.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Gift Shop",
		image = Image("LandmarksGroupB/labelled/gift_shop.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Homes for Sale",
		image = Image("LandmarksGroupB/labelled/homes_sale.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Limbo Lounge",
		image = Image("LandmarksGroupB/labelled/limbo_lounge.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Nail Time",
		image = Image("LandmarksGroupB/labelled/nail_time.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Photo Center",
		image = Image("LandmarksGroupB/labelled/photo_center.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Travel Shop",
		image = Image("LandmarksGroupB/labelled/travel_shop.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Video Services",
		image = Image("LandmarksGroupB/labelled/video_services.png"),
		category = 'labelled',
		width = 0.6,
		height = 0.6
	)
)

# landmark definitions...
distinctA = Pool(
	PoolDict(
		name = "Alton Place",
		image = Image("LandmarksGroupA/distinct/altonplace.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "Bright White",
		image = Image("LandmarksGroupA/distinct/bright_white.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "Curtis Center 1",
		image = Image("LandmarksGroupA/distinct/curtis_center_1.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "Fans",
		image = Image("LandmarksGroupA/distinct/fans.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Greek Columns",
		image = Image("LandmarksGroupA/distinct/greek_columns.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Grey Triangle",
		image = Image("LandmarksGroupA/distinct/grey_triangle.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Houston 1",
		image = Image("LandmarksGroupA/distinct/houston_1.png"),
		category = 'distinct',
		width = 0.8,
		height = 0.8
	),
	PoolDict(
		name = "House 2",
		image = Image("LandmarksGroupA/distinct/house2.png"),
		category = 'distinct',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "House 4",
		image = Image("LandmarksGroupA/distinct/house4.png"),
		category = 'distinct',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "Orange",
		image = Image("LandmarksGroupA/distinct/orange.png"),
		category = 'distinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Pub",
		image = Image("LandmarksGroupA/distinct/pub.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Roman Style",
		image = Image("LandmarksGroupA/distinct/roman_style.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Royal",
		image = Image("LandmarksGroupA/distinct/royal.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "Symphony",
		image = Image("LandmarksGroupA/distinct/symphony.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "White Columns",
		image = Image("LandmarksGroupA/distinct/white_columns.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	)
)

# landmark definitions...
distinctB = Pool(
	PoolDict(
		name = "Apartment",
		image = Image("LandmarksGroupB/distinct/apartment.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Church",
		image = Image("LandmarksGroupB/distinct/church.png"),
		category = 'distinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Egg Shape",
		image = Image("LandmarksGroupB/distinct/egg_shape.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "Fire House",
		image = Image("LandmarksGroupB/distinct/fire_house.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Green Stairs",
		image = Image("LandmarksGroupB/distinct/green_stairs.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "House 1",
		image = Image("LandmarksGroupB/distinct/house1.png"),
		category = 'distinct',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "House 3",
		image = Image("LandmarksGroupB/distinct/house3.png"),
		category = 'distinct',
		width = 0.6,
		height = 0.6
	),
	PoolDict(
		name = "House 7",
		image = Image("LandmarksGroupB/distinct/house7.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Mirrored",
		image = Image("LandmarksGroupB/distinct/mirrored.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Post Office",
		image = Image("LandmarksGroupB/distinct/post_office.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "Red Triangle",
		image = Image("LandmarksGroupB/distinct/red_triangle.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Round Brick",
		image = Image("LandmarksGroupB/distinct/round_brick.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Statues",
		image = Image("LandmarksGroupB/distinct/statues.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Tree Orange",
		image = Image("LandmarksGroupB/distinct/tree_orange.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Wooden Tiles",
		image = Image("LandmarksGroupB/distinct/wooden_tiles.png"),
		category = 'distinct',
		width = 0.9,
		height = 0.9
	)
)

# landmark definitions...
nondistinctA = Pool(
	PoolDict(
		name = "4034",
		image = Image("LandmarksGroupA/nondistinct/4034.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "American Flag",
		image = Image("LandmarksGroupA/nondistinct/american_flag.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Berklee Music",
		image = Image("LandmarksGroupA/nondistinct/berklee_music.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Big Tan",
		image = Image("LandmarksGroupA/nondistinct/big_tan.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Blueish",
		image = Image("LandmarksGroupA/nondistinct/blueish.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Brick Apartment",
		image = Image("LandmarksGroupA/nondistinct/brick_apartment.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Brick White Top",
		image = Image("LandmarksGroupA/nondistinct/brick_white_top.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Brown Grey Brick",
		image = Image("LandmarksGroupA/nondistinct/browngrey_brick.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Dirty Brick",
		image = Image("LandmarksGroupA/nondistinct/dirty_brick.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Fifteen Windows",
		image = Image("LandmarksGroupA/nondistinct/fifteen_windows.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Fleet",
		image = Image("LandmarksGroupA/nondistinct/fleet.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "Gate",
		image = Image("LandmarksGroupA/nondistinct/gate.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Grad Edu",
		image = Image("LandmarksGroupA/nondistinct/grad_edu.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Green Mirror Stripes",
		image = Image("LandmarksGroupA/nondistinct/green_mirror_stripes.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Grey Facade",
		image = Image("LandmarksGroupA/nondistinct/grey_facade.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Horiz Mirrors",
		image = Image("LandmarksGroupA/nondistinct/horiz_mirrors.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "House 5",
		image = Image("LandmarksGroupA/nondistinct/house5.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "House 8",
		image = Image("LandmarksGroupA/nondistinct/house8.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Little Columns",
		image = Image("LandmarksGroupA/nondistinct/little_columns.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Mendleton",
		image = Image("LandmarksGroupA/nondistinct/mendleton.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Old Brown",
		image = Image("LandmarksGroupA/nondistinct/old_brown.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "Pointy Windows",
		image = Image("LandmarksGroupA/nondistinct/pointywindows.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Red Brick Bush",
		image = Image("LandmarksGroupA/nondistinct/red_brick_bush.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Red White",
		image = Image("LandmarksGroupA/nondistinct/redwhite.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Shadows",
		image = Image("LandmarksGroupA/nondistinct/shadows.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Steps",
		image = Image("LandmarksGroupA/nondistinct/steps.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Tall Office",
		image = Image("LandmarksGroupA/nondistinct/tall_office.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Tan Bricks",
		image = Image("LandmarksGroupA/nondistinct/tan_bricks.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Two Doors Long",
		image = Image("LandmarksGroupA/nondistinct/two_doors_long.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Warehouse 2",
		image = Image("LandmarksGroupA/nondistinct/warehouse2.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "White",
		image = Image("LandmarksGroupA/nondistinct/white.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "White and Grey",
		image = Image("LandmarksGroupA/nondistinct/white_and_grey.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Wires",
		image = Image("LandmarksGroupA/nondistinct/wires.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Yeaa",
		image = Image("LandmarksGroupA/nondistinct/yeaa.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	)
)

# landmark definitions...
nondistinctB = Pool(
	PoolDict(
		name = "Adobe Columns",
		image = Image("LandmarksGroupB/nondistinct/adobe_columns.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Beach House",
		image = Image("LandmarksGroupB/nondistinct/beach_house.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Big Red",
		image = Image("LandmarksGroupB/nondistinct/big_red.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Blue",
		image = Image("LandmarksGroupB/nondistinct/blue.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Brick and Windows",
		image = Image("LandmarksGroupB/nondistinct/brick_and_windows.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Brick Stripes",
		image = Image("LandmarksGroupB/nondistinct/brick_stripes.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.45
	),
	PoolDict(
		name = "Brown",
		image = Image("LandmarksGroupB/nondistinct/brown.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Coolidge Corner",
		image = Image("LandmarksGroupB/nondistinct/coolidge_corner.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Dirty Concrete",
		image = Image("LandmarksGroupB/nondistinct/dirty_concrete.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Flags",
		image = Image("LandmarksGroupB/nondistinct/flags.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Flower",
		image = Image("LandmarksGroupB/nondistinct/flower.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Glass",
		image = Image("LandmarksGroupB/nondistinct/glass.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Greenish",
		image = Image("LandmarksGroupB/nondistinct/greenish.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Grey",
		image = Image("LandmarksGroupB/nondistinct/grey.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Hopefully Works Out",
		image = Image("LandmarksGroupB/nondistinct/hopefully_works_out.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Hotel 2",
		image = Image("LandmarksGroupB/nondistinct/hotel_2.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "House 6",
		image = Image("LandmarksGroupB/nondistinct/house6.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Limestone",
		image = Image("LandmarksGroupB/nondistinct/limestone.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Many Blocks",
		image = Image("LandmarksGroupB/nondistinct/manyblocks.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Nine Square Windows",
		image = Image("LandmarksGroupB/nondistinct/nine_square_windows.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Pipes",
		image = Image("LandmarksGroupB/nondistinct/pipes.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Red and White",
		image = Image("LandmarksGroupB/nondistinct/red_and_white.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Red Diamonds",
		image = Image("LandmarksGroupB/nondistinct/red_diamonds.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Regular",
		image = Image("LandmarksGroupB/nondistinct/regular.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Six Windows",
		image = Image("LandmarksGroupB/nondistinct/six_windows.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Stripe Mirror",
		image = Image("LandmarksGroupB/nondistinct/stripemirror.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Tan",
		image = Image("LandmarksGroupB/nondistinct/tan.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Triple Threat",
		image = Image("LandmarksGroupB/nondistinct/triple_threat.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Warehouse",
		image = Image("LandmarksGroupB/nondistinct/warehouse.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Warehouse 3",
		image = Image("LandmarksGroupB/nondistinct/warehouse3.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "White and Black",
		image = Image("LandmarksGroupB/nondistinct/white_and_black.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Windows",
		image = Image("LandmarksGroupB/nondistinct/Windows.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	),
	PoolDict(
		name = "Wood Frames",
		image = Image("LandmarksGroupB/nondistinct/wood_frames.png"),
		category = 'nondistinct',
		width = 0.45,
		height = 0.9
	),
	PoolDict(
		name = "Yellow",
		image = Image("LandmarksGroupB/nondistinct/yellow.png"),
		category = 'nondistinct',
		width = 0.9,
		height = 0.9
	)
)
