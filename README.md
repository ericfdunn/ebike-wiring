# ebike-wiring
 
A project to attach and wire headlights to my Pedego Ridge Rider

## Wiring Diagram

The first step is to plan the necessary components and wiring. The main battery is 48V (52V operating), so I need a voltage converter to supply the 12V necessary for the lighting. There is an existing headlight circuit built in to the bike's wiring, but it does not have sufficent power to run the new headlights and taillights. Instead, I will use it to control a relay that turns on the Daytime Running Lights, the tail lights, and energizes the circuits for the other lights.

See the wiring diagram [here](https://github.com/ericfdunn/ebike-wiring/blob/main/wiring%20diagram/wiring%20diagram.pdf)

Packaging was also limited, with only a small space available in the battery compartment, I unfortunately could not fit the relay there. The 48V supply will be run up to an enclosure on the handlebar with a relay before the voltage converter.

I don't yet know how I will trigger the brakelights. There are switches built into the brake levers that the computer uses to deactivate the motor, but the current on these switches is very small and I haven't come up with a way to piggyback off them for the rear brakelights.

## Assembly Pictures

Soldering the wires for the circuit board that connects the headlights and switches.
![d-image001.jpg](</images/d-image001.jpg>)

Backside.
![d-image002.jpg](</images/d-image002.jpg>)

Front with JST-XH connectors soldered. Attaching the XT60 connector for power.
![d-image003.jpg](</images/d-image003.jpg>)

Hot glue to cover any exposed connections, including the XT60 terminals underneath the collar.
![d-image004.jpg](</images/d-image004.jpg>)

I had to go back and add the diode after initial testing.
![d-image005.jpg](</images/d-image005.jpg>)

Power converted mounted onto the bottom of the project box using small machine screws. I roughly drilled some holes in the back to pass wires through.
![d-image006.jpg](</images/d-image006.jpg>)

Inside of the box with the power converter wires terminated with XT60 connectors.
![d-image007.jpg](</images/d-image007.jpg>)

Power delivery setup assembled. The relay has XT60 connectors to connect to the battery and power converter, and a smaller julliet pigtail that connects to the Pedego wiring harness's headlight circuit.
![d-image008.jpg](</images/d-image008.jpg>)

Making a power splitter that can connect to the batter. I got the juliet connectors from a spare battery bridge and pedego computer. It's not the most space-efficient connector, but this allows plug-in directly to the factory wiring harness.
![d-image010.jpg](</images/d-image010.jpg>)

Juliet pigtails tinned together and heatshrunk.
![d-image011.jpg](</images/d-image011.jpg>)

Then I soldierd the tinned leads into the XT60 connector.
![d-image012.jpg](</images/d-image012.jpg>)

Crimping JST-XH connectors to the headlights and headlight switch.
![d-image013.jpg](</images/d-image013.jpg>)

Testing the power converter with the bike battery to validate the voltage being delivered.
![d-image014.jpg](</images/d-image014.jpg>)

Bench testing the headlights. At this point I noticed that one of the ring lights was burnt out and I had to order a replacement.
![d-image015.jpg](</images/d-image015.jpg>)

Bench testing the driving lights.
![d-image016.jpg](</images/d-image016.jpg>)

Soldering the connectors on the wiring that will run from the battery compartment up to the handlebars.
![d-image017.jpg](</images/d-image017.jpg>)

Completed connector, hot glue applied and collar slid into place before heat shrinking.
![d-image018.jpg](</images/d-image018.jpg>)

Project mounted and wired under the handlebars.
![d-image019.jpg](</images/d-image019.jpg>)

Completed dasboard with project box closed up and hung under the handlebars with zip ties.
![d-image022.jpg](</images/d-image022.jpg>)

Ring lights on in the dark. They come on when I toggle on the lights from the Pedego controller. The three position switch on the handlebar controls the headlights individually. The brightness is great for nighttime riding and the beam pattern is D-shaped to keep the light focused down towards the roadway.
![d-image026.jpg](</images/d-image026.jpg>)

The final packing was a little rough, but I'm happy with the wiring and functionality. When I add in the tail lights, I may try to improve the packaging and routing of the wires.

## Parts List

Lights:
- [20W LED Motorcycle Fog Lights, 3 Inch Round LED Daytime Running Light](https://www.amazon.com/gp/product/B09VP3PT8P)
- [40W Motorcycle Tail Light Integrated Running Lamp Brake&Turn Signal](https://www.amazon.com/gp/product/B08NX56DNN)

Power delivery:
- [48V Step Down to DC 12V 20A 240W DC/DC Converter](https://www.amazon.com/gp/product/B089YBPHM1)
- [4 Pin DC 48V 40A Universal Car Vehicle Motor Fuse Relay](https://www.amazon.com/gp/product/B07QQKJLMD)
- [Car in line Fuse Holder 16AWG Cable with Built in Mini Spade Fuse](https://www.amazon.com/gp/product/B07RCG7RQX)
- [HKS Open Barrel Crimping Tool with 720PCS JST-XH Connectors Kit](https://www.amazon.com/dp/B0BY22GRNC?ref=ppx_yo2ov_dt_b_product_details&th=1)
- [20 Pair XT60H (XT60 Upgrade) Male Female Bullet Connectors](https://www.amazon.com/dp/B09ST768W2?psc=1&ref=ppx_yo2ov_dt_b_product_details)

 Project box:
- [Pocket Size Fishing Tackle Box](https://www.amazon.com/gp/product/B09S9VRM46)
- [PCB Board Prototype Kit for Electronic Projects](https://www.amazon.com/dp/B07PS4VCDD?psc=1&ref=ppx_yo2ov_dt_b_product_details)
