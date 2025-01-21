import magenta.music as mm

# Load a MIDI sequence
midi_data = mm.midi_file_to_note_sequence('path/to/midi/file.mid')

# Preprocess and convert MIDI to note sequence
note_seq = mm.extract_subsequence(midi_data, start_time=0, end_time=10)
melody_rnn = mm.models.melody_rnn.sequence_generator_bundle.read_bundle_file('melody_rnn')

# Generate a new melody
generated_sequence = melody_rnn.generate(note_seq, num_steps=128)
mm.sequence_proto_to_midi_file(generated_sequence, 'output_generated_melody.mid')
export LLVM_CONFIG=/usr/local/opt/llvm@7/bin/llvm-config
