# ebike-wiring
 
A project to attach and wire headlights to my Pedego Ridge Rider

## Wiring Diagram

The first step is to plan the necessary components and wiring. The main battery is 48V (52V operating), so I need a voltage converter to supply the 12V necessary for the lighting. There is an existing headlight circuit built in to the bike's wiring, but it does not have sufficent power to run the new headlights and taillights. Instead, I will use it to control a relay that turns on the Daytime Running Lights, the tail lights, and energizes the circuits for the other lights.

See the wiring diagram [here](https://github.com/ericfdunn/ebike-wiring/blob/main/wiring%20diagram/wiring%20diagram.pdf)

Packaging was also limited, with only a small space available in the battery compartment, I unfortunately could not fit the relay there. There will be a fuse located near the battery, and the 48V supply will be run up to an enclosure for the voltage converter on the handlebars.

I don't yet know how I will trigger the brakelights. There are switches built into the brake levers that the computer uses to deactivate the motor, but the current on these switches is very small and I haven't come up with a way to piggyback off them for the rear brakelights.

## Assembly Pictures

## Parts List

- [48V Step Down to DC 12V 20A 240W DC/DC Converter](https://www.amazon.com/gp/product/B089YBPHM1)
- [4 Pin DC 48V 40A Universal Car Vehicle Motor Fuse Relay](https://www.amazon.com/gp/product/B07QQKJLMD)
- [Car in line Fuse Holder 16AWG Cable with Built in Mini Spade Fuse](https://www.amazon.com/gp/product/B07RCG7RQX)
- [Pocket Size Fishing Tackle Box](https://www.amazon.com/gp/product/B09S9VRM46)
