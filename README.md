# Reaper-Surround

A collection of my mostly surround JSFX for the REAPER DAW ( www.reaper.fm ). Bugs/suggestions? File an issue or contact me on twitter/cockos forums/etc. Hopefully all of it should be made/modified by me. If it isn't, leave a comment & I'll remove.

Instructions
===
These are JSFX so DOWNLOAD ZIP & Put them in your Reaper EFFECTS folder. Note if you're cherry picking FX to DL (or updating), that you'll need surroundlib1-3 so get those too [1].

Disclaimer
===

NO warranty is provided, and these are provided as-is. Although I have been using these since 2015, I reserve the right to make changes, including backwards-incompatible changes. Although it is not in my intrest to do so, as I, too, have projects to keep working. Tools may be added, changed, or deleted at ANY time. Although old versions of this repo are available in the worst case. Experimental tools should be especially prone to change (pending my time & effort), and tools in **/Old** are prone to deletion/already deprecated/may be wrong.

Introduction to 15.1
===
* 15.1 is HQ channel-based INTERMEDIATARY format for 3D surround.
* Order as follows for 15.1: L R C LFE BL BR SL SR, HL HR, BtL BtR, HBL HBR HSL HSR
* Use  Reaper's channel parenting to place  stereo tracks statically.
* Use mono panners for dynamic panning of sounds (Mono panners are preferred as there is improved directivity with speaker playback)
* 15.1 Conversion to 3oA is supported for flexible & powerful workflows. However, ambisonics decoders for 3D speaker playback here are phantom, not full (i.e, don't include C). Try blue ripple's O3A suite or the http://www.matthiaskronlachner.com/?p=2015 ambix suite + https://www.york.ac.uk/sadie-project/ambidec.html if you need full or more decoders.

Quick start/Example workflows
===
* 3D: 1.0 to 15.1 Panner (S).txt >>> 15.1 to * downmix | 15.1 to 3oA Downmix (M).txt
* 3D Delivery: 15.1 to 7.x Downmix (M).txt for 11.1h (DTS-X) | 15.1 to 3D Downmix (M).txt for 9.1h (Auro3D, AMBEO speaker),  15.1 to 7.1 Downmix v2 (L).txt for 7.1 PL2z/DSU
* 3D Playback: 15.1 to 8.0 Speaker Tool (M).txt
* 2D: 7.1 Mono panner.txt >>> 7.1 to 5.1 Downmix (M).txt >>> 5.1 * >>> 5.1 to 2.0 Downmix (L).txt
* Mono track to center: 2.0 to 3.0 Upmix (C).txt
* 3oA FUMA: * to 3oA * Panner >>> 3oA Rotator (M).txt >>> * oA decoder

Note on sizes & CPU use
===
There may be different sizes of the same FX, eg, M(U)cro, (C)ommon, (S)mall, (M)edium, (L)arge, (X)tra Large. Different variations are provided for your convenience if CPU performance is of the utmost concern to you or if you are on a low-performance system (e.g, Atom, Celeron, etc). Obviously, a larger size of the same FX will provide more controls, but also more CPU consumption. On a fast CPU, each FX should use on average 1% of a core, or on a slow system, 5% of a core. The heaviest functions (those involving trig functions) should be optimized although it is not always possible to, and there is a balance to be struck between performance & code debt.

# Effects listing
 (for more info, refer to JSFX. It is advised to disable JSFX descriptions)

Ambisonics Panners
===
- 1.0 to 3oA 3D Panner (S).txt
- 2.0 to 3oA 2D Panner (M).txt
- 2.0 to 3oA 3D Panner (M).txt
- 15.1 to 1oA Downmix (L).txt (These 2 can convert 2.0 to 15.1 to ambisonics, as long as the channel order is correct, see above)
- 15.1 to 3oA Downmix (M).txt

Ambisonics Manipulators
===
- 3oA Rotator (M).txt: 2 rotators are provided for your convenience. To do a 360* spin starting from 0*, set offset to -180*, then adjust angle from -180* - +180*. You can use parameter modulation to automate Angle. Since Parameter modulation LFO may start at a undesired phase, offset is provided for manual adjustment (this was exactly the use-case for including 2 rotators). Or you can use a LFO on angle and a HFO on the offset for a wiggle.

Ambisonics Decoders (phantom)
===
- 15.1 Ambisonics decoder.txt (hand-tuned)
- 4 to 3 codec.txt (not really Ambisonics)
- 4.0 Ambisonics codec.txt (padded to 5.1)
- 7.1 Ambisonics decoder.txt
- 1oA 11.1bf decoder.txt (wrong)
- 1oA 3D cube decoder v3.txt
- 1oA prism.txt

Decoders are provided for your convenience but they're not that great.

Panners
===
- 1.0 to 15.1 Panner (S).txt
- 7.1 Mono Panner.txt
- 7.1 to 15.1 Height Panner v2 (M).txt


Upmixers (Experimental, except for "2.0 to 3.0 Upmix (C)")
===
Upmixers are considered experimental & are based on matrixes. It's advisable to use DTS Neural upmix (DTS edition like http://i54.tinypic.com/xq9xt5.png , NOT waves edition - waves has a bug with LFE). I've also tried about 10 other upmixers and they're all deficient in some way.

- 15.1 to 22.2 Upmix (U).txt
- 2.0 to 3.0 Upmix (C).txt
- 2.0 to 4.0 Upmix (M).txt
- 2.0 to 4.0 Upmix (U).txt
- 2.0 to 5.0 Upmix (M).txt
- 2.0 to 5.0 Upmix (U).txt
- 5.1 to 7.1 Upmix (U).txt
- 6.1 to 7.1 Upmix (M).txt

Manipulators
===
- 15.1 Width Control (M).txt
- 3.0 Spread Control (U).txt
- 5.1 Cross Width (S).txt
- 5.1 Level Control.txt
- 5.1 Mix Balance (C).txt
- 5.1 Mix Control (C).txt
- 5.1 Mix Control (M).txt
- 7.1 Depth Mixer (M).txt

Effects & Utility
===
- DifferenceMaker.txt
- dc_remove_6 & limiter_6: 6ch versions of existing JSFX.

For >6ch EQ & DC removal, I can recommend the excellent mcfx suite http://www.matthiaskronlachner.com/?p=1910 which can support 16ch.

Downmixers
===
- 15.1 to 3D Downmix (M).txt
- 15.1 to 5.1 Downmix (M).txt
- 15.1 to 7.1 Downmix (S).txt
- 15.1 to 7.1 Downmix v2 (L).txt
- 15.1 to 7.x Downmix (M).txt
- 5.1 to 2.0 Downmix (L).txt
- 7.1 to 5.1 Downmix (M).txt
- 7.1 to 6.0 Downmix (M).txt

Fixers
===
- Surcode Fixer (M).txt
- Surcode Fixer (S).txt
- Surround Fixer.txt

FX not listed might be old/WIP/specialist/for my own use.

FAQ
===

*How do I pan a sound flying directly overhead if your tools only seem to pan to the sides*?

You can (ab)use 5.1 Mix Control (M).txt as a X-Y panner, pan around in 7.1 then push it up & reduce width with 15.1 Width Control (M).txt, or play around with 1.0 to 3oA 3D Panner (S).txt. Elevation for 3oA 3D panners go from 0-180* for exactly this reason.

Future Directions
===
Changes MAY be made to Ambi FX (decoders & conventions), and upmixer FX, and MAY break.

[1]  I'm not asking you to download a 500mb electron app or a labyrinth of dependancies. Just 3 small text files.
