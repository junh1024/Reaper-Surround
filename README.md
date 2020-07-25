# Reaper-Surround

Introduction
---
A collection of mostly surround JSFX for the REAPER DAW ( www.reaper.fm ). These are JSFX so DOWNLOAD ZIP & Put them in your Reaper EFFECTS folder. Note if you're cherry picking FX, you'll probably need surroundlib so get those too [1]. Bugs/suggestions? File an issue or contact me on twitter.


Donations
---
Please PM me on cockos forums/reddit/Twitter/DC for donation info.

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
* 1.0 to 15.1 Panner GUI (M).txt
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

V1 & V2 upmixers are based on matrixes & are rudimentary so you either have:
- Wide back, no rear delay (downmix-compatible, but sounds bad cuz a wide back is distracting)
- Wide back, rear delay (NOT downmix-compatible, due to delay, stil sounds bad)
- Narrow back, no rear delay (VERY NOT downmix-compatible, due to polarity, stil sounds bad)
- Narrow back, rear delay  (NOT downmix-compatible, due to delay, sounds acceptable)

To totally avoid this dilemma, please use the V3 series FFT-based upmixers made in 2020.

### Note 3
**Sizes & CPU use**

There may be different sizes of the same FX, eg, M(U)cro, (C)ommon, (S)mall, (M)edium, (L)arge, (X)tra Large. Different variations are provided for your convenience if CPU performance is of the utmost concern to you or if you are on a low-performance system (e.g, Atom, Celeron, etc). Obviously, a larger size of the same FX will provide more controls, but also more CPU consumption. On a fast CPU, each FX should use on average 1% of a core, or on a slow system, 5% of a core.

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
- 1.0 to 15.1 Panner GUI (M).txt
- 7.1 to 15.1 Height Panner v2 (M).txt
- Surround Pan: 5.1 GUI panner courtesy of Sonic Anomaly. Doesn't work well with UI embedding in REAPER 6+ because the UI doesn't resize.
- "xtra surround panners.zip" has Sonic Anomaly's V2 & V3 (beta) panners. His V3 has 7.1 panning. These require REAPER 4.59+

Upmixers
---
Upmixers are considered experimental & are based on matrixes. It's advisable to use DTS Neural upmix (DTS edition like http://i54.tinypic.com/xq9xt5.png , NOT waves edition - waves has a bug with LFE). I've also tried about 10 other upmixers and they're all deficient in some way.

- 2.0 to 3.0 Upmix (C).txt
- 2.0 to 4.0 Upmix (M).txt: [Note 2](#note-2)
- 2.0 to 5.0 Upmix V2 (L).txt: 80% feature-complete DPL1-like surround upmixer, with more controls. [Note 1](#note-1), [Note 2](#note-2)
- 2.0 to 5.0 Upmix V3 (L).txt: (ALPHA) New upmix based on FFT [see FFT Notes](https://github.com/junh1024/Reaper-Surround#fft-notes) for maximum separation. It's Competitive with commercial upmixers. Features:
	- Basic image controls
	- Useful threshold controls which control the core algorithm, not 15 redundant controls that you can recreate in your DAW
	- Doesn't lie about PDC
	- Doesn't have an incorrect/downmix-incompatible bass level (bass is not moved/copied to LFE. It's blank.)
	- CPU optimized (CPU use depends on channel output)
	- 3 adjustable filters to increase rear separation, make it sound nicer, less distracting
	- mandatory 100% phase accuracy by design. No "faux phase accurate" mode which isn't even close
	- resizable UI which fits on small screens
- 5.1 to 7.1 Upmix (U).txt:
- 5.1 to 7.1 Upmix V2 (M).txt: These 2 5>7 upmixers are so rudimentary that they will probably have limited use. Side/Back balance uses the same mid/side detection as the 2>5 upmix. A balance control is provided for convenience, but may be 'bouncy' near the ends. [Note 1](#note-1)
- 5.1 to 7.1 Upmix V3 (M).txt: Using FFT  [see FFT Notes](https://github.com/junh1024/Reaper-Surround#fft-notes) to upmix 51 to 71. Since 71 is downmixed to 51 by combining the back 4,
	- Square mode isn't downmix compatible since it upscales the corner 4 to the side. For specialist use only.
	- Circle mode is downmix compatible since it re interprets the back 2 to back 4. Should work well on content downmixed from 61 or 71.
- 5.1 to 3D Upmix (L).txt: upmixes Using FFT [see FFT Notes](https://github.com/junh1024/Reaper-Surround#fft-notes) to height sounds that are closer to:
	- Ambience: 90*
	- Ambience +: 180*
	- Discrete SFX: the absolute center
	- Pan Slice: the pan slider
	- Function Designer: view the shape of the above mode
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
- FFT Tool suite: (ALPHA) Using FFT  (see FFT Notes). FFT Multi Tool works on dual stereo, but FFT Stereo Tool works on dual mono (or stereo) (planned). Because it's FFT, it's implicitly per-bin, not broadband.
	- Max & Min: selects and outputs Max/Min of the inputs (
	- Align (FPA): aligns the input to the sidechain
	- Subtract: subtracted from the input, is the sidechain. It's modified for a particular use-case. High frequencies will always have a Time Response of 1 to preserve transients & power , but low frequencies are controlled by the Time Response slider to reduce artefacts (at the expense of bleed). Frequency Response controls an additional subtraction of the HFs from 0=max, 1=none.
	- Phase limit: limits the Side so it' can't exceed the mid
	- Phase reflect: reflects >90* to <90* ie prevents antiphase
	- Noise Control/GF3 ARF: Controls the noise level. Noise is defined as a rolling spatio-average of the frequencies, Frequency Response & FFT Size is the averaging amount.
	- Transient: Controls the noise level. Transient is defined as louder than the previous frame (time).
	- Sustainizer: randomises phase-similar to DtBlkFx's smear mode:
	- Split-Combine Frequency: Amount controls a log frequency. Splits main & sidechain at the frequency, and combines the lower part of main with the upper part of sidechain.

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
To install Python for Windows, go to https://www.python.org/downloads/windows/  and download a 3.x version of Python. I suggest using a [version of Python](https://en.wikipedia.org/wiki/History_of_Python#Table_of_versions) that is around the time that your version of REAPER was released. REAPER 4.52 has been tested with python 3.1 & 3.5. If you're using REAPER 64bit you'll probably want a 64bit version of Python & vice versa. Afterwards, open the Reascript panel in REAPER preferences, and set the path & use to:

- python 3.1 x86 on Windows x64: C:\Windows\SysWOW64\ , python31.dll
- python 3.5 x86 on Windows x64: C:\Program Files (x86)\Python35 (or wherever you installed it), python35.dll

Then you're ready to go. Run a Reascript by going Actions > Show > Load, Run.

FFT Notes
---

**General FFT controls**
- Amount: to apply. Sometimes like a wet knob. >100% may not be unity.
- Cutoff: lowpass the processing, % of SR.
- Time Response: speed that the algorithm can respond from 1 (unrestricted) to 0 (frozen, may cause glitches). TR-- = artefacts--, but bleed++. Set to 0.5 @4K FFT Size, decreases with FFT Size for "2.0 to 5.0 Upmix V3 (L).txt", but adjustable in most other FX. Sensible values 0.5-1.
- Overlap: % of overlap of FFT segments. Overlap++ = CPU++ but artefacts--, % is approximate. See overlap_sel in surroundlibf.txt for exactl amount. It's fixed to 39.0625% in "2.0 to 5.0 Upmix V3 (L).txt", but adjustable in most other FX.
- FFT Size: length of FFT segments. In terms of 2^n, so 12 = 2^12 = 4096 (default). Size++ = artefacts--, but has little effect on CPU.

**Why is CPU so low?**

Reduction figures are approximate.

- CPU gating of algorithms: un-needed algorithms are switched off by conditionals. Mainly applies to "2.0 to 5.0 Upmix V3 (L).txt" -20% 
- CPU gating of metrics: un-needed statistics for the current algorithm are generally not measured. Data for GUI is not specifically measured & is generally required for the algorithm. -10%
- Staying in the cartesian domain, if possible: expensive trigonometric functions are avoided -30%
- Measuring less channels: For typical audio, what's happening in L is also happening in R, so measuring only 1 ch will get similar results. Mainly applies to "FFT Multi Tool (L).txt" -10%
- Linear-phase/unity design: Half the channels are processed, and the other half are obtained via subtraction of the result. This means the output MUST add up to the original. This saves some FFT & iFFT operations. Commercial vendors put whatever they want in any channel, and sometimes downmix- incompatible sounds, and it doesn't have to add up to the original. -20%
- Reduced bandwidth processing: up to 16-18k is processed by default. What's not processed may be moved to the secondary outputs in accordance with unity (above). You can ofc increase this to full. -15%
- Reduced overlap: New flexible architecture by [Tale](https://www.taletn.com/reaper/mono_synth/) in June. the default overlap (with a bell-shaped window) for nice-sounding FFT is 50%, but 40% (or less) with a trapezium window sounds just as good in many cases. -10%
- using memcpy & memset: -5%
- CPU gating during silence: functions are disabled as much as reasonable & not give artefacts during silence (only selected FX atm) -20% (depends on project)

**Why isn't CPU lower?**

- Not C++: JSFX is slow. +100%
- Conditionals: checks do take up CPU. +10%
- More buffers: the additional buffers for adjustable/reduced overlap. +5%
- GUI: +10%
- Functions: converting common snippets to functions in accordance with the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) makes for neater & maintainable code, but adds a measurable CPU increase with languages like JSFX +15%

**And?**

Conclusion: performance or quality is roughly on par with commercial implementations, but not necessarily simultaneously as you may need to make adjustments which increase CPU. My FFT FX typically use 10-15% of a 3Ghz core. If you're exporting long projects on a laptop on power-save mode, they'll do fine. Latency is also higher at a default of 4096sa compared with a typical 2048sa. Performance is balanced with quality, and if you want choice, you have ample control over otherwise "internal" or "unimportant" decisions which commercial vendors decide for you.

FAQ
---

*How do I pan a sound flying directly overhead if your tools only seem to pan to the sides*?

You can (ab)use 5.1 Mix Control (M).txt as a X-Y panner, pan around in 7.1 then push it up & reduce width with 15.1 Width Control (M).txt, or play around with 1.0 to 3oA 3D Panner (S).txt. Elevation for 3oA 3D panners go from 0-180* for exactly this reason. Or use "Surround Pan".

Future Directions
---
Changes MAY be made to Ambi FX (decoders & conventions), and upmixer FX, and MAY break.

[1]  I'm not asking you to download a 500mb electron app or a labyrinth of dependancies. Just 3 small text files.
