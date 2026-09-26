# 🎵 BeatStream (DT Music) — Premium iOS-Inspired Android Music Client

[![Platform](https://img.shields.io/badge/Platform-Android-green.svg?style=for-the-badge&logo=android)](https://developer.android.com)
[![Kotlin](https://img.shields.io/badge/Kotlin-1.9.0-blue.svg?style=for-the-badge&logo=kotlin)](https://kotlinlang.org)
[![Compose](https://img.shields.io/badge/Jetpack%20Compose-M3-purple.svg?style=for-the-badge&logo=jetpackcompose)](https://developer.android.com/jetpack/compose)
[![Database](https://img.shields.io/badge/Database-Room%20%2F%20SQLite-orange.svg?style=for-the-badge&logo=sqlite)](https://developer.android.com/training/data-storage/room)
[![API](https://img.shields.io/badge/Lyrics_API-LRCLIB-blueviolet.svg?style=for-the-badge)]()

**BeatStream (DT Music)** is an enterprise-grade, highly polished Android music streaming and local playback client. Built with **100% Jetpack Compose (Material 3)**, it seamlessly blends a premium **iOS / Apple Music aesthetic** with powerful local catalog scanning, offline track downloading, real-time karaoke lyrics sync, and hardware-accelerated audio enhancement.

---

## 📖 What is BeatStream? (What the App Does)

BeatStream is designed to be a complete, unified music hub for Android. Instead of forcing you to choose between online streaming services and your own local physical files, **BeatStream integrates both into a single cohesive interface**. 

The application serves three primary functions:
1. **Dynamic High-Fidelity Streaming:** Instantly searches, indexes, and streams over 50 million tracks from the iTunes online music database at a master quality bitrate of **320 kbps**.
2. **Offline Audio Synchronizer:** Lets you download any online stream as a high-bitrate physical MP3 file onto your device's sandbox. It automatically shifts to offline local playback when network connectivity is lost.
3. **Local Library Manager:** Scans your device's physical storage for local music files (e.g., download folder, SD card) and displays them alongside your cloud playlists.

---

## 🛠️ How to Use the App (Comprehensive Guide)

### 1. Navigating the Home Feed
* **Discover Music:** When you launch the app, you are greeted by the home screen featuring a curated **Hero Music Banner** showcasing trending artists and dynamic carousel grids of trending songs, recommended albums, and followed artists.
* **1-Tap Quick Play:** Tap on any song row in the trending list to immediately boot up the master audio engine and start playback.
* **Instant Action Pills:** At the top of any Album, Playlist, or Artist detail page, use the side-by-side **Play** (starts sequentially) and **Shuffle** (instantly randomizes queue) twin pill buttons.

### 2. Searching and Online Discovery
* **Live Global Search:** Tap the search bar on the Home or Search screens. As you type, the app searches both your local library database and the live iTunes online server.
* **Category Filters:** Filter results instantly by **All**, **Songs**, **Albums**, or **Artists** using the horizontal chip selectors.
* **Context Options (3-Dot Menu):** Tap the 3-dot menu icon on any song row to open the context sheet. From there, you can add it to custom playlists, append it to your active queue, or download it.

### 3. Creating and Managing Playlists
* **Create a Playlist:** Go to the **Library** tab, tap **"New Playlist"**, and enter a custom title and description.
* **Add Songs Inline:** While playing a song or browsing search results, tap the 3-dot icon -> **"Add to Playlist"**. You can select an existing playlist or create a brand new one directly from the popup dialog without leaving your current screen.
* **Manage Tracks:** Inside any custom playlist, you can remove individual tracks, update the playlist description, or delete the entire playlist with confirmation prompts.

### 4. Listening in Offline Mode (Downloading Songs)
* **High-Speed Downloads:** Tap the 3-dot menu on any online track and select **"Download Track"**. The app initiates an asynchronous high-speed network download of the MP3 stream, displaying a live progress indicator.
* **Automatic Offline Caching:** Once downloaded, the track is permanently saved to your device's physical sandbox, and a green download badge is applied to the track.
* **Lossless Playback:** When playing a downloaded track, the app automatically reads the local file, saving battery life and internet data. Go to the **Library -> Downloads** section to view your physical music inventory.

### 5. Customizing Your Aesthetic & Sound
* **True OLED Black Theme:** Perfect for late-night listening and saving AMOLED screen battery.
* **Clean iOS Light Theme:** Offers grouped layouts (`#F2F2F7`) and frosted translucent glass panels matching iOS Apple Music.
* **Accent Colors:** Go to the **Library -> Settings** section to customize your premium accent colors (Signature iOS Red, Apple Mint, Electric Violet, System Blue, Sunset Orange).
* **Material You Dynamic Theming:** Turn on **Dynamic Wallpaper Mode** (Android 12+) to let BeatStream extract colors from your system phone theme!
* **Hardware AudioFX Booster:** Integrated directly into Settings, allowing you to toggle the hardware **LoudnessEnhancer DSP** for deeper bass, rich acoustic presence, and studio-clear vocal projection.

### 6. Interactive Karaoke Lyrics
* **Synced Karaoke Deck:** While a track is playing, slide up the Now Playing screen and tap the **Lyrics** button.
* **Auto Sync:** The app queries the LRCLIB server for synchronized LRC lyrics.
* **Tap-to-Navigate:** Lines of lyrics scroll automatically as the artist sings. Lyrics are styled with heavy contrast, making it easy to read and sing along.

---

## 🎨 Design System Highlights

BeatStream implements a bespoke **iOS Design System** built completely from scratch using Compose primitives:
* **The Squircle (Continuous Curvature):** Unlike standard Android rounded corners, all artworks and playlist cards utilize squircles (smooth curvature corner layouts) for a ultra-premium look.
* **Frosted Glass (Blur Layers):** The floating mini-player pill and bottom navigation bar utilize alpha transparencies and high-fidelity shadow compositions, creating a translucent overlay depth.
* **Liquid Animations:** Micro-interactions, such as the animated audio wave visualizer next to the active track and transition page-swipes, make navigation incredibly smooth.

---

## 🏗️ Architecture & Technical Stack

```
   ┌─────────────────────────────────────────────────────────┐
   │                       UI LAYER                          │
   │   Jetpack Compose (M3)  │  StateFlow  │  ViewModels     │
   └────────────────────┬────────────────────────┬───────────┘
                        │                        │
                        v                        v
   ┌─────────────────────────────────────────────────────────┐
   │                     BUSINESS LAYER                      │
   │               MusicRepository  │  AudioPlayerManager    │
   └────────────────────┬────────────────────────┬───────────┘
                        │                        │
                        v                        v
   ┌────────────────────────────────────────┐ ┌──────────────┐
   │                    DATA LAYER          │ │ AUDIO ENGINE │
   │  Room DB (SQLite)  │  Retrofit APIs    │ │ MediaPlayer  │
   │  Local File Cache  │  Coil Image Sync  │ │ AudioFX DSP  │
   └────────────────────┴───────────────────┘ └──────────────┘
```

* **Clean MVVM Architecture:** Separates visual presentation entirely from core repository business logic.
* **Robust Flow Concatenation:** Combines local tracks, online tracks, and query filters asynchronously using Kotlin `Flow.combine()` and `debounce` to eliminate typing lag.
* **Dynamic Database Migrations:** Employs `.fallbackToDestructiveMigration()` inside the `AppDatabase` configuration, preventing database conflicts or crashes during upgrades.
* **Safe Threading:** Strict offloading of database writes, API downloads, and artwork streaming to `Dispatchers.IO` using structured Coroutines.

---

## 💾 Database Schema

BeatStream uses a relational **SQLite Database** managed via Jetpack Room:

* **`tracks`**: Stores catalog metadata (ID, title, artist, album, audio URL, artwork URL, playback statistics, local download file paths).
* **`playlists`**: Manages user-created custom playlist headers.
* **`playlist_tracks`**: Junction table (cross-reference) mapping songs to playlists with manual sort indexing.
* **`liked_tracks`**: Keeps track of track IDs liked by the user.
* **`listening_history`**: Holds listening history stamps for the "Recently Played" algorithm.
* **`downloaded_tracks`**: Stores verified offline sandbox paths for high-bitrate physical MP3 files.
* **`user_profiles`**: Retains user profile settings, equalizer presets, selected accent themes, and dark/light system configurations.

---

## 🏁 Development Setup

### Prerequisites
* **Android Studio Ladybug** (or newer)
* **JDK 17** configured in your System and Android Studio.
* **Android SDK Build-Tools 34.0.0**

### Local Build and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dt-music-beatstream.git
   cd dt-music-beatstream
   ```
2. Compile and run standard unit tests to ensure configuration integrity:
   ```bash
   ./gradlew testDebugUnitTest
   ```
3. Assemble the debug APK:
   ```bash
   ./gradlew assembleDebug
   ```
4. Install and run on your target Android device or emulator:
   ```bash
   ./gradlew installDebug
   ```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
