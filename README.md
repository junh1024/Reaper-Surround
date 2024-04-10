# Reaper-Surround

Introduction
---
A collection of mostly surround JSFX for the REAPER DAW ( www.reaper.fm ). These are JSFX so **[CLICK HERE TO DOWNLOAD ZIP](https://github.com/junh1024/Reaper-Surround/archive/master.zip)** & extract ALL of the zip into your Reaper EFFECTS folder.

You can find the containing folder in REAPER by going **Options > Show REAPER resource path**. Alternatively, the direct paths:

Windows:

- C:/Users/USERNAME/AppData/Roaming/REAPER/Effects (for normal install)
- REAPER/Effects (for portable install)

Mac:

- HOMEFOLDER/Library/Application Support/REAPER/Effects

It is advised to ENABLE **"options > show in FX list > JSFX filename"** in your FX browser, as I refer to them by name. Bugs/suggestions? File an [issue](https://github.com/junh1024/Reaper-Surround/issues) ,  or contact me on [twitter](https://twitter.com/junh1024/) .

Alternatively, [this video](https://www.youtube.com/watch?v=9EegrN-gF5o) shows how to install JSFX.

Donations
---
Surround is just a hobby for me since 2014. If you use them (especially commercially), you are encouraged to donate. By CC (securely handled by stripe) on https://donorbox.org/junh1024 to encourage further development & lets me know they are genuinely useful for work. Also, contact me for custom development based on my stuff.


![img](https://i.imgur.com/eDlWKrf.png)

Disclaimer
---
NO warranty is provided, and these are provided as-is. Although I have been using these since 2014, I reserve the right to make changes, including backwards-incompatible changes, although I try not to as I also have projects to keep working. Tools may be added, changed, or deleted at ANY time. Although old versions of this repo are available in the worst case. Alpha/beta tools are especially prone to change, tools in /Old are deprecated.

Introduction to 15.1
---

![15.1](https://i.imgur.com/0H320GZ.png)

* 15.1 is HQ channel-based system for 3D surround, based on combining the best of NHK's 22.2, and 7.1 surround.
* It is 7.1.6.2 in Dolby notation.
* Order as follows for 15.1: L R C LFE BL BR SL SR, HL HR, BtL BtR, HBL HBR HSL HSR (extends SMPTE 5.1)
* It's intended to be a HQ intermediary for mixing in 3D surround, and "Multi Mix Convert (L).txt" is included to downmix to formats such as Auro3D 5.1.4, DTS-X Base & MPEG-H 7.1.4, and Atmos CBA 9.1.6
* Mixing in one of the above formats and converting to another could result in an inferior conversion, hence a format such as my 15.1 is ideal due to a reasonable channel layout.
* 15.1 Conversion to 3oA is supported for flexible & powerful workflows. FUMA Ambisonics decoders for 3D speaker playback here are included, but are very basic.
* Use mono panners for dynamic panning of sounds (Mono panners are preferred as there is improved directivity with speaker playback)
* Use Reaper's [channel parenting](http://d2zjg0qo565n2.cloudfront.net/sites/default/files/focusrite/Screen%20Shot%202015-06-10%20at%2014.42.00.png) to place stereo tracks statically.

Quick start/Example workflow tools
---
### 2D workflow:
* 1.0 to 5.1 Panner GUI (L).txt
* 2.0 to 5.0 Upmix V3 (S).txt
* < 5.1 Effects & manipulators >
* 5.1 to 2.0 Downmix (L).txt

### 3D workflow:
* 1.0 to 15.1 Panner GUI (L).txt for mono sources
- 2.0 to 15.1 Mapper (M).txt for stereo sources
* 5.1 to 3D Upmix (L).txt
* Multi Mix Convert (L).txt


### FUMA Ambisonics workflow:
- 1.0 to 3oA 3D Panner (S).txt
- 2.0 to 3oA 2D Panner (M).txt
- 3oA Rotator (M).txt
- 15.1 Ambisonics decoder.txt	(phantom)
- 7.1 Ambisonics decoder.txt	(phantom)
- 4.0 Ambisonics codec.txt		(phantom)

### Stereo beatmaking:
- FFT Multi Tool (L).txt: Noise/Transient control for creative use
- FFT Stereo Tool (L).txt: Phase limit/reflect modes to tame your width

# Effects listing
Listed below are the most common/useful effects. For more info, refer to JSFX.

Ambisonics Panners (FUMA)
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
- 1oA 3D cube decoder v1.txt

Decoders are provided for your convenience but they're not that great.

Panners
---
- 1.0 to 3.1 Panner (M).txt: 3.0 front surround panner, with width control. Move & Copy actions are supported for LFE use, and  Mixing & Monitoring modes for a total of 4 combinations. The specification for LFE in digital mixes, is to gain it by 10dB on playback. Hence while mixing, it is gained by -10dB. For monitoring, this is not applied.
- 1.0 to 5.1 Panner GUI (L).txt
- 1.0 to 15.1 Panner GUI (L).txt
- 2.0 to 15.1 Mapper (M).txt
- 7.1 to 15.1 Height Panner v2 (M).txt

Upmixers
---
Upmixers are considered experimental, based on matrix or FFT.

- 2.0 to 3.0 Upmix (C).txt (manual upmixer, all the others are automatic)
- 2.0 to 5.0 Upmix V2 (L).txt: 80% feature-complete DPL1-like surround upmixer with 0 audio latency, but a behavioral latency [Note 1](#note-1) . It works best as LCR upmixer [Note 2](#note-2), and that's the new default as of 2024.
- 2.0 to 5.0 Upmix V3 (S).txt: Upmix based on FFT for maximum separation. [see FFT Notes](#fft-notes) for controls & explanation. It's Competitive with commercial upmixers. Features:
	- Basic image controls
	- Doesn't lie about PDC
	- Doesn't have an incorrect/downmix-incompatible bass level (bass is not moved/copied to LFE. It's blank.)
	- CPU optimized (CPU use depends on channel output)
	- Mandatory phase-accurate by design. No "faux phase-accurate" mode which doesn't add to unity
- 2.0 to 5.0 Upmix V3 (L).txt: Above, plus
	- Threshold controls which control the core algorithm, not 10 redundant controls that you can recreate in your DAW
	- Adjustable filters to increase rear separation, make it sound nicer, less distracting
	- resizable UI which fits on small screens
- 5.1 to 7.1 Upmix (U).txt:
- 5.1 to 7.1 Upmix V2 (L).txt: These 2 5>7 upmixers are so rudimentary that they will probably have limited use. Side/Back balance uses the same mid/side detection as the 2>5 upmix. A balance control is provided for convenience, but may be 'bouncy' near the ends. [Note 1](#note-1)
- 5.1 to 7.1 Upmix V3 (L).txt: Using FFT [see FFT Notes](#fft-notes) to upmix 51 to 71. Since 71 is downmixed to 51 by combining the back 4,
	- Circle mode is summation downmix compatible since it re-interprets the back 2 to back 4. Circle+ also analyses the front channels for more accurate interpretation of the soundfield.
	- Square mode isn't summation downmix compatible since it upscales the corner 4 to the side by extracting content panned midway.
- 5.1 to 3D Upmix (L).txt: upmixes Using FFT [see FFT Notes](#fft-notes) to height sounds that are closer to:
	- Ambience: 90*. Sounds are reflected downwards after that. Sounds are more evenly upmixed.
	- Ambience +: 180*. Wider sounds are upmixed more.
	- Discrete SFX: the absolute center. The visualizer shows the soundfield.
	- Pan Slice: the pan slider. The visualizer shows the front/back balance of the frequencies.
	- Function Designer: view the shape of the above mode
- 6.1 to 7.1 Upmix (M).txt

Manipulators
---
- 3.0 Spread Control (U).txt
- 5.1 Level Control.txt
- 5.1 Mix Control (M).txt
- 15.1 Width Control (M).txt

Downmixers
---
- 5.1 to 2.0 Downmix (L).txt
- 7.1 to 5.1 Downmix (M).txt
- 15.1 to 5.1 Downmix (M).txt
- 15.1 to 7.1 Downmix (S).txt
- **Multi Mix Convert (L).txt** can convert between many surround formats like 5.1, 7.1, 5.1.2, Auro3D & AMBEO 5.1.4, Atmos Base 7.1.2, DTS-X Base & MPEG-H 7.1.4, Atmos 9.1.6, and 22.2 NHK. It internally converts to 15.1, so speakers which aren't in 15.1 will get downmixed.
- 15.1 to 8.0 Speaker Tool (M).txt (8.0h Order: L R, HL HR, BL BR, SL SR, which is similar & backwards compatible with SMPTE-MS 7.1, for 3D surround playback using commonly available 7.1 sound cards)

![8.0sh](https://i.imgur.com/1nivgkz.png)

Effects (Audio)
---
- compressor_6.txt: multichannel compressor, intended as a long-term compressor (ie, leveler). Works for 16ch, but you can type in more. As the key & affector are all selected channels, it's suitable for holistic compression of ambisonics. [Note 1](#note-1)
- dc_remove_6: DC remover for 6ch
- limiter_6: limiter (or clipper) for 6ch
- loop_slicer_multi.txt: beat-synced realtime loop slicer, which sequentially splits slices up to 4x stereo, according to split length
- Pitch Tracker 2 (X).txt:  Compared to the original, adds PDC, off mode, automation out, removes MIDI out & gfx
- StereoField V2.txt: Compared to the original, the rotation is expanded to +- 180 deg, and width is processed before rotation, so DPL and SFR is now much easier

Effects (MIDI)
---
- KeyTracker 2 (M).txt: shows current MIDI note via slider. Use with PMOD for adding movement/width to a song.
- midi_chorderizer V2.txt: Compared to the original, a 0 offset mutes the note, and fixes the velocity bug. Replaces my earlier buggy "Octaver (S).txt"

Effects (Third-Party, external)
---
- EQ 16ch: please use the mcfx suite from http://www.matthiaskronlachner.com/?p=1910
- Reverb 64ch:  please use fdnReverb from https://plugins.iem.at/
- Sonic Anomaly's other JSFX are available https://github.com/Sonic-Anomaly/Sonic-Anomaly-JSFX/tree/master/Plugins or in ReaPack

Meters & Analysis
---
- Channel Similarity Meter (S).txt: Analysis of channel similarity based on FFT. Selection of 2/16ch input available.
- gfxGoniometer V2.txt: A traditional phase vectorscope for stereo analysis. Compared to the original, adds automatic scaling of input, pan analysis, 2/16ch input selector for analysing surround, removes rays.

Specialist & Utility
---
- Bitutils V2 can be used to change the volume of a signal in small or large amounts using the volume & shift sliders respectively. Shift should be bitperfect. The bitdepth can also be reduced to reduce size when encoding to compressed lossless codecs. The channels slider goes up to 16 by you can type in any number.
- DifferenceMaker.txt: subtracts Sidechain (3+4) from  Main (1+2). Useful for getting the difference after an effect.
- MSEDDouble.txt: Double Mid/Side Codec (1+2) & (5+6)
- Pan Zone V2.txt: Freeform FFT stereo imager (originally by Keith Handy). V2 adds more controls, more intuition, GUI, and PDC.
- Simple Crossfade.txt: Fade between 2 sets of inputs, like a DJ mixer.
- Surcode Fixer: Fixes delay &/ PDC, width adjustments of Surcode DPL.
- Surround Fixer.txt
- FFT Tool suite: (ALPHA) Using FFT  (see FFT Notes). FFT Multi Tool works on dual stereo, but FFT Stereo Tool works on dual mono (or stereo) (planned). Because it's FFT, it's implicitly per-bin, not broadband.
	- Max & Min: selects and outputs Max/Min of the inputs (
	- Align (FPA): aligns the input to the sidechain
	- Subtract: subtracted from the input, is the sidechain. It's modified for a particular use-case. High frequencies will always have a Time Response of 1 to preserve transients & power , but low frequencies are controlled by the Time Response slider to reduce artefacts (at the expense of bleed). Frequency Response controls an additional subtraction of the HFs from 0=max, 1=none.
	- Noise Control/GF3 ARF: Controls the noise level. Noise is defined as a rolling spatio-average of the frequencies, Frequency Response & FFT Size is the averaging amount.
	- Transient: Adds or reduces transients. Transient is defined as louder than the previous frame (time).
	- Sustain: Adds sustain. Sustain is defined as softer than the previous frame.
	- Phase limit: limits the Side so it' can't exceed the mid
	- Phase reflect: reflects >90* to <90* ie prevents antiphase
	- Sustainizer: randomises phase-similar to DtBlkFx's smear mode:
	- Split-Combine Frequency: Amount controls a log frequency. Splits main & sidechain at the frequency, and combines the lower part of main with the upper part of sidechain.

# Scripts
	
Scripts for General Use
---
- Delete item fades under threshold.py: By default, RPR makes small (10ms) fades on item boundaries to prevent artefacts, which is usually a good thing. But when you're making a continuous edit from pieces, these automatic fades can actually introduce artefacts. This script is useful in this case, as it deletes fades under 20ms, for selected items.
- ProjectSanitizer.py
- Reaper Stats.py: collects various project statistics and outputs them via a dialog. See script for more details.
- Set item start to position.py
- SetPanAccordingToName.py: Useful for implementing directional dialogue for films.
- Bitperfect Take Gain.py: You can set the gain of items directly, in a bitperfect way with this (not an adjustment/offset). Note that 1 bit = 6.02 dB (approx).
- Set Envelope Points.py: this script sets the value for all selected envelope points, not just the 1st one

Scripts for Remixing
---
- Set item [BPM](#bpm).py: This is intended for *mashups & mixes*. In the case of your item BPM differing from your project BPM you want to stretch the item to fit your project. This script makes it quick, just input the BPM of selected item(s), and it will handle the maths. REAPER actually has no concept of item BPM so this is done via play rate & timebase.
- Set item BPM_sequential.py: Sets the BPM of multiple items sequentially, with individual user input
- Round item BPM.py: Rounds the BPM of a clip. After several project BPM changes, the BPM/playrate can become approximate (like 127.999) due to the imprecision of floating point. This rounds them. NB: deliberate BPMs like 128.2 will also get rounded so be careful which clips to apply it.
- Get item BPM.py: This is intended to be used in mixes. You can get the BPM of a single item, but this is intended to be used at the completion of a mix, as you can calculate the WEIGHTED average BPM of multiple items so that you can set a better project BPM.

- Adjust Take Pitch.py: If you're playing around with item pitches in say, a mashup, you might find this useful. If you have items with different pitches, you can adjust them by the same offset.

### REAPER to FFMPEG edit
Lossless editing of lossy audio. Edit visually using the REAPER DAW, this script generates FFMPEG commands which will perform the editing. REAPER supports many codecs and containers of avi, mp4, mkv. If your audio isn't supported, you can edit a mp3 proxy in REAPER, and change the command yourself afterwards.

You will have FFMPEG in your PATH, REAPER installed, and Python Reascript set up.
See https://github.com/junh1024/Reaper-Surround#reascript-python-setup-for-windows

Notes:
- Only simple editing supported. No gain/fades, rate changes, etc
- You MUST fill in any gaps/silences yourself
- All clips must be on a single track
- Multiple different input files may work (as long as they're the same specification), but it's not tested
- Editing isn't perfectly accurate on lossy codecs. There is a *fudge_factor* which you can adjust to decrease the length of clips
- If FFMPEG produces a broken file, try downgrading your FFMPEG
- I'm not responsible if commands get corrupted on your clipboard

Instructions:

We are going to kill 2 birds with 1 stone, and install FFMPEG for [REAPER](https://www.reaper.fm/download.php) (so that you can open arbitrary video files in REAPER) and Windows (so that you can run FFMPEG commands in windows). I've not tested this exact version or process, as I've already got the equivalent set up via other means.

1. Download [FFMPEG](https://github.com/GyanD/codexffmpeg/releases/download/4.4/ffmpeg-4.4-full_build-shared.zip)
2. Inside the zip, there is a bin folder with exes & DLLs. Extract these to your REAPER User Plugins folder, which might be C:\Program Files\REAPER\UserPlugins or C:\Program Files\REAPER\Installdata\Plugins . Whichever exists, depending on how & where you installed REAPER
3. Add the REAPER Plugins folder to your [Windows User Path Environment Variable](https://windowsloop.com/install-ffmpeg-windows-10/) . Start from step 3.3 of the guide
4. Open REAPER , and edit your clips as necessary
5. Press shift-? to open the actions pallete
5. New action > Load Reascript , and choose the [script](https://raw.githubusercontent.com/junh1024/Reaper-Surround/master/Scripts/REAPER%20to%20FFMPEG%20edit.py) , which you will have saved on your PC.
6. Right click and drag around to select the edited clips
7. Choose the "REAPER to FFMPEG edit" script, and Run the script
8. Copy the commands out of the message box
9. Run the commands for FFMPEG in the windows command prompt


Reascript Python Setup for Windows
---
To install Python for Windows, go to https://www.python.org/downloads/windows/  and download a 3.x version of Python. I suggest using a [version of Python](https://en.wikipedia.org/wiki/History_of_Python#Table_of_versions) that is around the time that your version of REAPER was released, or 3.1-3.9. REAPER 4.52 has been tested with python 3.1 & 3.5. If you're using REAPER 64bit you'll probably want a 64bit version of Python & vice versa. Afterwards, open the Reascript panel in REAPER preferences, and set the path & use to:

- python 3.1 x86 on Windows x64: C:\Windows\SysWOW64\ , python31.dll
- python 3.5 x86 on Windows x64: C:\Program Files (x86)\Python35 (or wherever you installed it), python35.dll

Then you're ready to go. Run a Reascript by going Actions > Show > Load, Run.


## VST Compatibility

### Windows VST2 users

VST2 Compatibility for windows is achieved through ReaJS. You can then run some FX in your favorite DAW (surround FX may not work in some hosts) or perhaps live in Equalizer APO.

1. Install Reaplugs 64bit https://www.reaper.fm/reaplugs/ into your VST2 folder, Example: "C:\Program Files\VSTPlugIns"
2. Navigate into the Reaplugs directory, and download [this file](https://github.com/junh1024/Reaper-Surround/releases/download/0.2105/reajs.ini) in there. Example: the downloaded reajs.ini , goes into C:\Program Files\VSTPlugIns\Reaplugs\
3. Open reajs.ini and change the rootpath to where the ReaPlugs JS folder is. Example:  "C:\Program Files\VSTPlugIns\Reaplugs\JS" . If you're using exactly the path as per step 1, this is already set.
4. Change the file to these if using surround. Use 8 for 7.1. If you want exactly 7.1, this is already set.
```
inputs=8    ; number of audio inputs (0-64)
outputs=8    ; number of audio outputs (0-64)
```
5. Extract [this zip](https://github.com/junh1024/Reaper-Surround/archive/master.zip) into your ReaPlugs JS Effects folder, such that it sits beside other Effects folders. Example: C:\Program Files\VSTPlugIns\Reaplugs\JS\Effects\Reaper-Surround Master\
6. Load the ReaJS plugin into your host, and press "Load" to select the Effects under Reaper-Surround

### Mac/VST3 users

You will need to use [**YSFX**](https://github.com/JoepVanlier/ysfx/releases/tag/v0.0.2) and extract the VST3 into:

- Windows: C:\Program Files\Common Files\VST3
- Mac: Library\Audio\Plug-ins\VST

Unfortunately, YSFX has [FFT issues](https://github.com/jpcima/ysfx/issues/66) so it rules out most of the interesting ones, and has trouble finding dependencies. I've made a small archive of 2 interesting FX & their dependancies for YSFX users [**here**](https://github.com/junh1024/Reaper-Surround/releases/download/0.2105/Reaper-Surround-YSFX.zip) .

### AAX Compatibility
AAX Compatibility for Pro Tools Windows is limited due to the FILM order for channels and limited options for channel count. I haven't tested this.

6. Follow steps 1-5 as for "Windows VST2 users"
7. Insert ReaJS in a VST to AAX loader like DDMF metaplugin
8. Insert the loader into a 2 or 6ch track
9. Load ReaJS into your loader and select your FX
10. If a 5.1 surround FX was selected previously, load another ReaJS, select "Multi Mix Convert (L).txt", and select 5.1 SMPTE input, 5.1 FILM output.

## mcfx_convolver presets
After installing mcfx_convolver16 from the [mcfx](https://www.matthiaskronlachner.com/?p=1910) suite, and **[the zip of my repo](https://github.com/junh1024/Reaper-Surround/archive/master.zip)** , my convolver_presets folder goes in "C:\Users\USERNAME\AppData\Roaming\mcfx\", or "~/Library/mcfx/" on Mac OS X. You may need to [unhide]( https://osxdaily.com/2011/07/22/access-user-library-folder-in-os-x-lion/
) your library folder on Mac. The presets can now be opened by mcfx_convolver16 in your DAW. It's recommended to uncheck "save preset within project" in mcfx_convolver, and then "save preset as default" in RPR so projects don't grow unnecessarily large.

- HSV_A_Testbench.conf is a template for loading IRs in the Hesuvi 7ch order. Please modify it according to the filename of your IR. The input is 7.1 SMPTE-Microsoft order.
- HSV_B_Testbench.conf same, except 14ch
- SADIE2-KEMAR-DFC-714SD-48K.conf is in the SMPTE-Dolby order, according to the Dolby document [Additional Audio Channels and Soundfields for Immersive Audio](https://developer.dolby.com/globalassets/technology/atmos/additional-channels-for-immersive-audio.pdf) p4
- SADIE2-KEMAR-DFC-714SM-PC-48K.conf is in the SMPTE-Microsoft order, according to Microsoft [WAVEFORMATEXTENSIBLE](https://learn.microsoft.com/en-us/windows/win32/api/mmreg/ns-mmreg-waveformatextensible)
- SADIE2-KEMAR samples are courtesy of the [SADIE 2 database](https://www.york.ac.uk/sadie-project/database.html) . These IRs [are](https://www.mdpi.com/2076-3417/8/11/2029) , [DFC equalized](https://github.com/kcat/openal-soft/issues/806#issuecomment-1377034577) , and use Phantom Center, but [aren't tightly synced](https://cdn.discordapp.com/attachments/547440061478862850/1107489215811432578/image.png) . This shouldn't pose a problem unless you're using DS/DPL1-like upmixing.
- BBCRD is courtesy of [BBC RD](https://github.com/bbc/bbcrd-brirs/blob/master/README.md)

### Note 1
**Block-based effects**

These effects analyse a chunk of audio, then make a decision. The audio is not delayed, but the reaction is delayed by half a blocksize. This is done for performance & audio stability reasons. These are NOT based on FFT. To make it react on time would be a big hassle with PDC due to differing paths, for small benefit & hence isn't implemented. The minimum blocksize that happens in practice is set in Reaper preferences under Audio Device.
* A low blocksize makes it change faster, and a high response makes it change more, so these 2 things make it behave quicker. A high blocksize would make reactions happen abruptly, hence blocksize is a suggested 2048 or lower (23+ blocks/sec @48k)
* A high response allows faster changes, and a low response allows smaller changes. A response that is too high will make the changes unstable, hence response shouldn't go above 0.3

I have tried to set sensible defaults.

### Note 2
**Surround upmixers**

V1 & V2 upmixers are based on matrixes & are rudimentary so you either have:
- Wide back, no rear delay (downmix-compatible, but sounds bad cuz a wide back is distracting)
- Wide back, rear delay (NOT downmix-compatible, due to delay, still sounds bad)
- Narrow back, no rear delay (VERY NOT downmix-compatible, due to polarity, still sounds bad)
- Narrow back, rear delay  (NOT downmix-compatible, due to delay, sounds acceptable)

To totally avoid this dilemma, please use the V3 series FFT-based upmixers made in 2020.

### Note 3
**Sizes & CPU use**

There may be different sizes of the same FX, eg, M(U)cro, (C)ommon, (S)mall, (M)edium, (L)arge, (X)tra Large. Different variations are provided for your convenience if CPU performance is of the utmost concern to you or if you are on a low-performance system (e.g, Atom, Celeron, etc). Obviously, a larger size of the same FX will provide more controls, but also more CPU consumption. On a fast CPU, each FX should use on average 1% of a core, or on a slow system, 5% of a core.

FFT Notes
---

**General surround controls**
- Width: Center into Front
- Depth: mix Rear into Front or vice-versa
- Rear threshold/crossover: threshold/crossover to move sounds into rear, depending on phase of bins
- Rear width/lowpass/transients: self-explanatory

**General FFT controls**
- Amount: to apply. Sometimes like a wet knob. >100% may not be unity.
- Cutoff: lowpass the processing, % of SR. May save CPU.
- Time Response: speed that the algorithm can respond from 1 (unrestricted) to 0 (frozen, may cause glitches). TR-- = artefacts--, but bleed++. Set to 0.5 @4K FFT Size, decreases with FFT Size for "2.0 to 5.0 Upmix V3 (L).txt", but adjustable in most other FX. Sensible values 0.5-1.
- FFT Size: length of FFT segments. In terms of 2^n, so 12 = 2^12 = 4096 (default). Size++ = artefacts--, frequency resolution/separation++, temporal resolution--, PDC++ (latency), but has little effect on CPU.

**Why is CPU so low?**

Reduction figures are approximate.

- CPU gating of algorithms: un-needed algorithms are switched off by conditionals. Mainly applies to "2.0 to 5.0 Upmix V3 (L).txt" -20% 
- CPU gating of metrics: un-needed statistics for the current algorithm are generally not measured. Data for GUI is not specifically measured & is generally required for the algorithm. -10%
- Staying in the cartesian domain, if possible: expensive trigonometric functions are avoided -30%
- Measuring less channels: For typical audio, what's happening in L is also happening in R, so measuring only 1 ch will get similar results. Mainly applies to "FFT Multi Tool (L).txt" -10%
- Linear-phase/unity design: Half the channels are processed, and the other half are obtained via subtraction of the result. This means the output MUST add up to the original. This saves some FFT & iFFT operations. Commercial vendors put whatever they want in any channel, and sometimes downmix- incompatible sounds, and it doesn't have to add up to the original. -20%
- Reduced bandwidth processing: up to 16-18k is processed by default. What's not processed may be moved to the secondary outputs in accordance with unity (above). You can ofc increase this to full. -15%
- using memcpy & memset: -5%
- CPU gating during silence: functions are disabled as much as reasonable & not give artefacts during silence (only selected FX atm) -20% (depends on project)

**Why isn't CPU lower?**

- Not C++: JSFX is slow. +100%
- Conditionals: checks do take up CPU. +10%
- GUI: +10%
- Functions: converting common snippets to functions in accordance with the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) makes for neater & maintainable code, but adds a measurable CPU increase with languages like JSFX +15%

**And?**

Conclusion: performance or quality is roughly on par with commercial implementations, but not necessarily simultaneously as you may need to make adjustments which increase CPU. My FFT FX typically use 10-15% of a 3Ghz core. If you're exporting long projects on a laptop on power-save mode, they'll do fine. Latency is also higher at a default of 4096sa compared with a typical 2048sa. Performance is balanced with quality, and if you want choice, you have ample control over otherwise "internal" or "unimportant" decisions which commercial vendors decide for you.
