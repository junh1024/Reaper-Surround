# Reaper-Surround

Introduction
---
A collection of mostly surround JSFX for the REAPER DAW ( www.reaper.fm ). These are JSFX so DOWNLOAD ZIP & Put them in your Reaper EFFECTS folder. Note if you're cherry picking FX to DL (or updating), that you'll need surroundlib1-3 so get those too [1]. Bugs/suggestions? File an issue or contact me on twitter.

Disclaimer
---
NO warranty is provided, and these are provided as-is. Although I have been using these since 2015, I reserve the right to make changes, including backwards-incompatible changes. Although it is not in my intrest to do so, as I, too, have projects to keep working. Tools may be added, changed, or deleted at ANY time. Although old versions of this repo are available in the worst case. Experimental tools should be especially prone to change (pending my time & effort), and tools in **/Old** are prone to deletion/already deprecated/may be wrong. Some FX may have unused controls, which are TBD.

Introduction to 15.1
---

![15.1](https://i.imgur.com/0H320GZ.png)

* 15.1 is HQ channel-based system for 3D surround, based on combining the best of NHK's 22.2, and 7.1 surround.
* Best used as an intermediary, since delivery of 15.1 is tricky.
* Order as follows for 15.1: L R C LFE BL BR SL SR, HL HR, BtL BtR, HBL HBR HSL HSR (applies to 5.1/7.1 too)
* Use Reaper's channel parenting to place stereo tracks statically.
* Use mono panners for dynamic panning of sounds (Mono panners are preferred as there is improved directivity with speaker playback)
* 15.1 Conversion to 3oA is supported for flexible & powerful workflows. However, ambisonics decoders for 3D speaker playback here are phantom, not full (i.e, don't include C). You will need to convert Fuma to Ambix, then find an Ambix decoder.

Quick start/Example workflow tools
---
### 2D workflow:
* 3.1 Panner (M).txt (for center channel dialog, front SFX, and LFE use), 7.1 Mono panner.txt (for phantom center & surround panning), 7.1 to 5.1 Downmix (M).txt
* Surround Pan (5.1 GUI panner)
* < 5.1 Effects & manipulators >
* 5.1 to 2.0 Downmix (L).txt

### 3D workflow:
* 1.0 to 15.1 Panner (S).txt
* 15.1 to 7.1 Downmix v2 (L).txt
* 15.1 to 8.0 Speaker Tool (M).txt
* 15.1 to 3oA Downmix (M).txt
* 15.1 to 7.x Downmix (M).txt (11.1h/7.1.4 DTS-X) or 15.1 to 3D Downmix (M).txt (9.1h/5.1.4 Auro3D, AMBEO speaker)

### Fuma Ambisonics workflow:
- 1.0 to 3oA 3D Panner (S).txt
- 2.0 to 3oA 2D Panner (M).txt
- 3oA Rotator (M).txt
- 15.1 Ambisonics decoder.txt	(phantom)
- 7.1 Ambisonics decoder.txt	(phantom)
- 4.0 Ambisonics codec.txt		(phantom)

### Note 1
**Block-based effects**

These effects analyse a chunk of audio, then make a decision. The audio is not delayed, but the reaction is delayed by half a blocksize. This is done for performance & audio stability reasons. These are NOT based on FFT. To make it react on time would be a big hassle with PDC due to differing pathes, for small benefit & hence isn't implemented. The minimum blocksize that happens in practice is set in Reaper preferences under Audio Device.
* A small block makes it change faster, and a high response makes it change more, so these 2 things make it behave quicker.
* A big blocksize would make reactions happen inappropriately, hence blocksize is a suggested 2048 or lower (23+ blocks/sec @48k)
* A high response would make the audio unstable, hence response shouldn't go above 0.3

I have tried to set sensible defaults.

### Note 2
**Surround upmixers**

As said above, these are based on matrixes & are rudimentary, as such they come with ceveats & compromises. The back channels, by default, are purely the side channel of the original. When decoded to stereo, the are completely wide & out of phase. Wide sounds at the back is distracting, hence the default is to reverse the polarity of 1 channel, and make it narrow, pleasing, and undistracting. Unfortunately, this has the effect of making a downmix being lopsided & the surround image sounding strange, so a delay is applied to decorrelate the front & back further. This makes the surround image acceptable, at the cost of phasing when downmixed. A wide back with no delay is, however, downmix-compatible. You may need to change the polarity depending on the depth slider. Controls are provided for convenience but I can't guarantee you won't abuse them to make bad sound. The best I can do is explain the compromises above.

### Note 3
**Sizes & CPU use**

There may be different sizes of the same FX, eg, M(U)cro, (C)ommon, (S)mall, (M)edium, (L)arge, (X)tra Large. Different variations are provided for your convenience if CPU performance is of the utmost concern to you or if you are on a low-performance system (e.g, Atom, Celeron, etc). Obviously, a larger size of the same FX will provide more controls, but also more CPU consumption. On a fast CPU, each FX should use on average 1% of a core, or on a slow system, 5% of a core. The heaviest functions (those involving trig functions) should be optimized although it is not always possible to, and there is a balance to be struck between performance & code debt.

# Effects listing
Listed below are the most common/useful effects. For more info, refer to JSFX. It is advised to disable JSFX descriptions.

Ambisonics Panners (FuMa)
---
- 1.0 to 3oA 3D Panner (S).txt
- 2.0 to 3oA 2D Panner (M).txt
- 2.0 to 3oA 3D Panner (M).txt
- 15.1 to 3oA Downmix (M).txt (convert 2.0 to 15.1 to ambisonics, as long as the channel order is correct, see above)

Ambisonics Manipulators
---
- 3oA Rotator (M).txt: 2 rotators are provided for your convenience. To do a 360* spin starting from 0*, set offset to -180*, then adjust angle from -180* - +180*. You can use parameter modulation to automate Angle. Since Parameter modulation LFO may start at a undesired phase, offset is provided for manual adjustment (this was exactly the use-case for including 2 rotators). Or you can use a LFO on angle and a HFO on the offset for a wiggle.

Ambisonics Decoders (phantom)
---
- 15.1 Ambisonics decoder.txt (hand-tuned)
- 7.1 Ambisonics decoder.txt
- 4.0 Ambisonics codec.txt (padded to 5.1)
- 1oA 11.1bf decoder.txt (wrong)
- 1oA 3D cube decoder v3.txt
- 1oA prism.txt

Decoders are provided for your convenience but they're not that great.

Panners
---
- 3.1 Panner (M).txt: 3.0 front surround panner, with width control. Move & Copy actions are supported for LFE use, and  Mixing & Monitoring modes for a total of 4 combinations. The specification for LFE in digital mixes, is to gain it by 10dB on playback. Hence while mixing, it is gained by -10dB. For monitoring, this is not applied.
- 7.1 Mono Panner.txt
- 1.0 to 15.1 Panner (S).txt
- 7.1 to 15.1 Height Panner v2 (M).txt
- Surround Pan: 5.1 GUI panner courtesy of Sonic Anomaly. Doesn't work well with UI embedding in REAPER 6+ because the UI doesn't resize.
- "xtra surround panners.zip" has Sonic Anomaly's V2 & V3 (beta) panners. His V3 has 7.1 panning. These require REAPER 4.59+

Upmixers
---
Upmixers are considered experimental & are based on matrixes. It's advisable to use DTS Neural upmix (DTS edition like http://i54.tinypic.com/xq9xt5.png , NOT waves edition - waves has a bug with LFE). I've also tried about 10 other upmixers and they're all deficient in some way.

- 2.0 to 3.0 Upmix (C).txt
- 2.0 to 4.0 Upmix (M).txt: [Note 2](#note-2)
- 2.0 to 5.0 Upmix V2 (L).txt: 80% feature-complete DPL1-like surround upmixer, with more controls. [Note 1](#note-1), [Note 2](#note-2)
- 5.1 to 7.1 Upmix (U).txt:
- 5.1 to 7.1 Upmix V2 (M).txt: These 2 5>7 upmixers are so rudimentary that they will probably have limited use. Side/Back balance uses the same mid/side detection as the 2>5 upmix. A balance control is provided for convenience, but may be 'bouncy' near the ends. [Note 1](#note-1)
- 6.1 to 7.1 Upmix (M).txt
- 15.1 to 22.2 Upmix (U).txt



Manipulators
---
- 3.0 Spread Control (U).txt
- 5.1 Level Control.txt
- 5.1 Mix Balance (C).txt
- 5.1 Mix Control (M).txt
- 15.1 Width Control (M).txt

Downmixers
---
- 5.1 to 2.0 Downmix (L).txt
- 7.1 to 5.1 Downmix (M).txt
- 15.1 to 5.1 Downmix (M).txt
- 15.1 to 7.1 Downmix (S).txt
- 15.1 to 7.1 Downmix v2 (L).txt
- 15.1 to 7.x Downmix (M).txt
- 15.1 to 3D Downmix (M).txt
- 15.1 to 8.0 Speaker Tool (M).txt (8.0h Order: L R, HL HR, BL BR, SL SR, which is similar & backwards compatible with SMPTE-MS 7.1, for 3D surround playback using commonly available 7.1 sound cards)

![8.0sh](https://i.imgur.com/1nivgkz.png)

Effects (Audio)
---
- dc_remove_6: DC remover for 6ch
- limiter_6: limiter (or clipper) for 6ch
- compressor_6.txt: multichannel compressor, intended as a long-term compressor (ie, leveler). Works for 16ch, but you can type in more. As the key & affector are all selected channels, it's suitable for holistic compression of ambisonics. [Note 1](#note-1)
- loop_slicer_6.txt: beat-synced realtime loop slicer, which sequentially splits slices up to 4x stereo, according to split length

Effects (MIDI)
---
- KeyTracker 2 (M).txt: shows current MIDI note via slider. Use with PMOD for adding movement/width to a song.
- Octaver (S).txt

Effects (Third-Party, external)
---
- EQ 16ch: please use the mcfx suite from http://www.matthiaskronlachner.com/?p=1910
- Reverb 64ch:  please use fdnReverb from https://plugins.iem.at/
- Sonic Anomaly's other JSFX are available https://github.com/Sonic-Anomaly/Sonic-Anomaly-JSFX/tree/master/Plugins or in ReaPack

Specialist & Utility
---
- DifferenceMaker.txt: subtracts Sidechain (3+4) from  Main (1+2). Useful for getting the difference after an effect.
- Peak_Extender_SC.txt: Extends the peaks of Main (1+2) with the Sidechain (3+4). Use case: combining a lossless low-DR song with a lossy high-DR song. Clipping artefacts? Verify both songs are aligned & levels set correctly.
- MSEDDouble.txt: Double Mid/Side Codec (1+2) & (5+6)
- Simple Crossfade.txt: Fade between 2 sets of inputs, like a DJ mixer.
- Surcode Fixer: Fixes delay &/ PDC, width adjustments of Surcode DPL.
- Surround Fixer.txt

Scripts
---
- Delete item fades under threshold.py: By default, RPR makes small (10ms) fades on item boundaries to  prevent artefacts, which is usually a good thing. But when you're making a continuous edit from pieces, these automatic fades can actually introduce artefacts. This script is useful in this case, as it deletes fades under 20ms, for selected items.
- ProjectSanitizer.py
- Reaper Stats.py: collects various project statistics and outputs them via a dialog. See script for more details.
- Set item start to position.py
- SetPanAccordingToName.py: Useful for implementing directional dialogue for films.

- Set item [BPM](#bpm).py: This is intended for *mashups & mixes*. In the case of your item BPM differing from your project BPM you want to strech the item to fit your project. This script makes it quick, just input the BPM of selected item(s), and it will handle the maths. REAPER actually has no concept of item BPM so this is done via play rate & timebase.
- Get item BPM.py: This is intended to be used in mixes. You can get the BPM of a single item, but this is intended to be used at the completion of a mix, as you can calculate the WEIGHTED average BPM of multiple items so that you can set a better project BPM. Note that this is appropriate due to the imprecision of floating point. 

- Adjust Take Pitch.py: If you're playing around with item pitches in say, a mashup, you might find this useful. If you have items with different pitches, you can adjust them by the same offset.
- Bitperfect Take Gain.py: You can set the gain of items directly, in a bitperfect way with this (not an adjustment/offset). Note that 1 bit = 6.02 dB (approx). 

Reascript Python Setup for Windows
---
To install Python for Windows, go to https://www.python.org/downloads/windows/  and download a 3.x version of Python. I suggest using a version of Python that is around the time that your version of REAPER was released. I'm using py 3.1 with REAPER 4.52 but it's probably possible to use newer ones.

If you're using REAPER 64bit you'll probably want a 64bit version of Python & vice versa. Afterwards, open the Reascript panel in REAPER preferences, and set the path to C:\Windows\SysWOW64\ (32bit) or C:\Windows\System32 (64bit) and the python DLL should be detected. Then you're ready to go.

Run a Reascript by going Actions > Show > Load, Run.

FAQ
---

*How do I pan a sound flying directly overhead if your tools only seem to pan to the sides*?

You can (ab)use 5.1 Mix Control (M).txt as a X-Y panner, pan around in 7.1 then push it up & reduce width with 15.1 Width Control (M).txt, or play around with 1.0 to 3oA 3D Panner (S).txt. Elevation for 3oA 3D panners go from 0-180* for exactly this reason. Or use "Surround Pan".

Future Directions
---
Changes MAY be made to Ambi FX (decoders & conventions), and upmixer FX, and MAY break.

[1]  I'm not asking you to download a 500mb electron app or a labyrinth of dependancies. Just 3 small text files.
