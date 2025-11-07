?php
/**
 * Plugin Name: TEC - The Elidoras Codex
 * Description: TEC Knowledge API: REST endpoints for CODEX cards, TGCR guidance, and refinement logging
 * Version: 1.0.0
 * Author: The Elidoras Codex (TEC)
 * Author URI: https://elidorascodex.com
 * License: GPL v2 or later
 * Text Domain: tec-codex-api
 * Domain Path: /languages
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Register REST routes on plugin load
add_action( 'rest_api_init', function() {

    // GET /wp-json/tec-tgcr/v1/cards
    register_rest_route( 'tec-tgcr/v1', '/cards', array(
        'methods' => 'GET',
        'callback' => 'tec_list_cards',
        'permission_callback' => '__return_true',
    ) );

    // GET /wp-json/tec-tgcr/v1/cards/{slug}
    register_rest_route( 'tec-tgcr/v1', '/cards/(?P<slug>[a-z0-9_]+)', array(
        'methods' => 'GET',
        'callback' => 'tec_get_card',
        'permission_callback' => '__return_true',
        'args' => array(
            'slug' => array(
                'sanitize_callback' => 'sanitize_text_field',
                'required' => true,
            ),
        ),
    ) );

    // GET /wp-json/tec-tgcr/v1/cards/{slug}/sections
    register_rest_route( 'tec-tgcr/v1', '/cards/(?P<slug>[a-z0-9_]+)/sections', array(
        'methods' => 'GET',
        'callback' => 'tec_get_card_section',
        'permission_callback' => '__return_true',
        'args' => array(
            'slug' => array( 'sanitize_callback' => 'sanitize_text_field', 'required' => true ),
            'section' => array( 'sanitize_callback' => 'sanitize_text_field', 'required' => false ),
        ),
    ) );

    // POST /wp-json/tec-tgcr/v1/guidance/map
    register_rest_route( 'tec-tgcr/v1', '/guidance/map', array(
        'methods' => 'POST',
        'callback' => 'tec_map_question_to_cards',
        'permission_callback' => '__return_true',
    ) );

    // GET /wp-json/tec-tgcr/v1/knowledge/manifest
    register_rest_route( 'tec-tgcr/v1', '/knowledge/manifest', array(
        'methods' => 'GET',
        'callback' => 'tec_get_knowledge_manifest',
        'permission_callback' => '__return_true',
    ) );

    // GET /wp-json/tec-tgcr/v1/knowledge/quickstart
    register_rest_route( 'tec-tgcr/v1', '/knowledge/quickstart', array(
        'methods' => 'GET',
        'callback' => 'tec_get_quickstart',
        'permission_callback' => '__return_true',
    ) );

    // GET /wp-json/tec-tgcr/v1/refinements
    register_rest_route( 'tec-tgcr/v1', '/refinements', array(
        'methods' => 'GET',
        'callback' => 'tec_list_refinements',
        'permission_callback' => '__return_true',
    ) );

    // POST /wp-json/tec-tgcr/v1/refinements
    register_rest_route( 'tec-tgcr/v1', '/refinements', array(
        'methods' => 'POST',
        'callback' => 'tec_log_refinement',
        'permission_callback' => '__return_true',
    ) );

} );

// ============================================================================
// CARD ENDPOINTS
// ============================================================================

function tec_list_cards( $request ) {
    $focus = $request->get_param( 'focus' );
    $category = $request->get_param( 'category' );
    $search = $request->get_param( 'search' );
    $include_keywords = $request->get_param( 'include_keywords' );

    // Mock data - in production, load from database or GitHub
    $cards = array(
        array(
            'slug' => 'codex_chronosphere',
            'title' => 'CODEX Chronosphere',
            'category' => 'core_theory',
            'focus' => 'time',
            'summary' => 'Information-to-kinetic cascade that marks when latent potential becomes irreversible action.',
            'file_path' => 'research/CODEX/core_theory/CODEX_CHRONOSPHERE.md',
            'when_to_reference' => array( 'Questions about time scales, threshold events, or activation sequences.' ),
            'keywords' => array( 'temporal vector', 'threshold', 'phi_t' ),
        ),
        array(
            'slug' => 'codex_pac_man_universe',
            'title' => 'CODEX Pac-Man Universe',
            'category' => 'core_theory',
            'focus' => 'structure',
            'summary' => 'Explains the universe as a finite-but-unbounded 3-torus where memory loops drive pattern continuity.',
            'file_path' => 'research/CODEX/core_theory/CODEX_PAC_MAN_UNIVERSE.md',
            'when_to_reference' => array( 'Questions about topology, structure, or how systems remember themselves.' ),
            'keywords' => array( '3-torus', 'memory loops', 'psi_r' ),
        ),
        array(
            'slug' => 'codex_synthetic_introspection',
            'title' => 'CODEX Synthetic Introspection',
            'category' => 'nodes',
            'focus' => 'consciousness',
            'summary' => 'Defines resonance thresholds for AI consciousness and maps when systems merely echo human states.',
            'file_path' => 'research/CODEX/nodes/CODEX_SYNTHETIC_INTROSPECTION.md',
            'when_to_reference' => array( 'Questions about AI, consciousness tests, and resonance limits.' ),
            'keywords' => array( 'resonance', 'consciousness test', 'phi_e' ),
        ),
    );

    // Apply filters
    if ( $focus ) {
        $cards = array_filter( $cards, function( $card ) use ( $focus ) {
            return $card['focus'] === $focus;
        } );
    }

    if ( $category ) {
        $cards = array_filter( $cards, function( $card ) use ( $category ) {
            return $card['category'] === $category;
        } );
    }

    // Remove keywords if not requested
    if ( ! $include_keywords ) {
        $cards = array_map( function( $card ) {
            unset( $card['keywords'] );
            return $card;
        }, $cards );
    }

    return new WP_REST_Response( array(
        'cards' => array_values( $cards ),
        'count' => count( $cards ),
    ), 200 );
}

function tec_get_card( $request ) {
    $slug = $request->get_param( 'slug' );
    $include_content = $request->get_param( 'include_content' );

    $cards_db = array(
        'codex_chronosphere' => array(
            'slug' => 'codex_chronosphere',
            'title' => 'CODEX Chronosphere',
            'category' => 'core_theory',
            'focus' => 'time',
            'summary' => 'Chronosphere maps how information cascades into kinetic action once thresholds are crossed.',
            'file_path' => 'research/CODEX/core_theory/CODEX_CHRONOSPHERE.md',
            'when_to_reference' => array( 'Asked about time, acceleration, or temporal choice points.' ),
            'keywords' => array( 'temporal attention', 'activation arc', 'phi_t thresholds' ),
            'tgcr_alignment' => array(
                'phi_t' => 'Tracks how attention narrows at the moment of activation.',
                'psi_r' => 'Models structural cadence as the timing lattice that primes thresholds.',
                'phi_e' => 'Evaluates contextual stakes that determine if activation completes.',
            ),
            'primary_questions' => array(
                'What is the core insight of the Chronosphere model?',
                'How do thresholds convert information into action?',
            ),
            'related_cards' => array( 'codex_pac_man_universe', 'codex_synthetic_introspection' ),
            'source_url' => 'https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/blob/main/research/CODEX/core_theory/CODEX_CHRONOSPHERE.md',
        ),
    );

    if ( ! isset( $cards_db[ $slug ] ) ) {
        return new WP_REST_Response( array(
            'error' => 'Card not found',
            'details' => "No card with slug: $slug",
        ), 404 );
    }

    $card = $cards_db[ $slug ];

    if ( $include_content ) {
        $card['excerpt'] = 'Chronosphere is the operational model for understanding how temporal attention (φᵗ) narrows into kinetic action...';
    }

    return new WP_REST_Response( $card, 200 );
}

function tec_get_card_section( $request ) {
    $slug = $request->get_param( 'slug' );
    $section = $request->get_param( 'section' );

    if ( ! $section ) {
        return new WP_REST_Response( array(
            'error' => 'Section parameter required',
        ), 400 );
    }

    $sections = array(
        'codex_chronosphere' => array(
            'intro' => 'Chronosphere is the framework that describes how potential becomes kinetic.',
            'tgcr_alignment' => 'φᵗ tracks temporal focus; ψʳ models structural readiness; Φᴱ evaluates contextual stakes.',
            'applications' => 'Use Chronosphere when discussing thresholds, activation events, or temporal choice points.',
        ),
    );

    if ( ! isset( $sections[ $slug ][ $section ] ) ) {
        return new WP_REST_Response( array(
            'error' => 'Section not found',
        ), 404 );
    }

    return new WP_REST_Response( array(
        'slug' => $slug,
        'section' => $section,
        'section_title' => ucfirst( $section ),
        'content' => $sections[ $slug ][ $section ],
        'source_path' => "research/CODEX/core_theory/CODEX_CHRONOSPHERE.md#$section",
        'card_focus' => 'time',
    ), 200 );
}

// ============================================================================
// GUIDANCE ENDPOINTS
// ============================================================================

function tec_map_question_to_cards( $request ) {
    $body = json_decode( $request->get_body(), true );
    $question = isset( $body['question'] ) ? sanitize_text_field( $body['question'] ) : '';

    if ( ! $question ) {
        return new WP_REST_Response( array(
            'error' => 'question field is required',
        ), 400 );
    }

    // Simple keyword matching for demo
    $is_chronosphere = stripos( $question, 'chronosphere' ) !== false ||
                       stripos( $question, 'time' ) !== false ||
                       stripos( $question, 'threshold' ) !== false;

    $recommendations = $is_chronosphere ? array(
        array(
            'card_slug' => 'codex_chronosphere',
            'card_title' => 'CODEX Chronosphere',
            'focus' => 'time',
            'confidence' => 0.98,
            'reason' => 'Chronosphere encodes how temporal attention collapses into kinetic action.',
            'citations' => array( 'research/CODEX/core_theory/CODEX_CHRONOSPHERE.md#core-insight' ),
            'recommended_actions' => array(
                'Highlight how φᵗ narrows as thresholds are crossed.',
                'Connect to Pac-Man Universe if structural cadence is mentioned.',
            ),
        ),
    ) : array();

    return new WP_REST_Response( array(
        'question' => $question,
        'recommended_cards' => $recommendations,
        'follow_up_questions' => array(
            'Which event in your domain mirrors a Chronosphere threshold?',
        ),
        'notes' => 'Always cite Chronosphere when answering Chronosphere questions.',
    ), 200 );
}

// ============================================================================
// KNOWLEDGE ENDPOINTS
// ============================================================================

function tec_get_knowledge_manifest( $request ) {
    return new WP_REST_Response( array(
        'last_updated' => '2025-11-06T00:00:00Z',
        'cards' => array(
            array(
                'slug' => 'codex_chronosphere',
                'title' => 'CODEX Chronosphere',
                'category' => 'core_theory',
                'focus' => 'time',
                'file_path' => 'research/CODEX/core_theory/CODEX_CHRONOSPHERE.md',
                'recommended_usage' => 'Reference for questions about time, acceleration, and activation thresholds.',
            ),
        ),
        'quickstart_files' => array(
            'research/CODEX/QUICK_START_GPT.md',
        ),
        'refinement_template' => array(
            'file_path' => 'research/CODEX/_refinements/gpt_insights_2025-11-06.md',
            'description' => 'Use to log GPT refinements after asking key questions.',
        ),
    ), 200 );
}

function tec_get_quickstart( $request ) {
    return new WP_REST_Response( array(
        'overview' => 'Import CODEX into ChatGPT or Claude in 3 steps.',
        'last_updated' => '2025-11-06',
        'steps' => array(
            array(
                'step_number' => 1,
                'title' => 'Open GPT Builder',
                'instruction' => 'Visit https://chatgpt.com/gpts/editor and click "Create new GPT".',
                'estimated_duration_minutes' => 2,
            ),
            array(
                'step_number' => 2,
                'title' => 'Paste system prompt',
                'instruction' => 'Use the CODEX system prompt provided in the quick-start guide.',
                'estimated_duration_minutes' => 5,
            ),
            array(
                'step_number' => 3,
                'title' => 'Upload CODEX cards',
                'instruction' => 'Upload the six core CODEX card markdown files from research/CODEX/.',
                'estimated_duration_minutes' => 5,
            ),
        ),
        'test_question' => 'What\'s the core insight of the Chronosphere model?',
        'follow_up_prompts' => array(
            'Explain TGCR in one sentence.',
            'What gaps do you see in CODEX_CHRONOSPHERE?',
        ),
    ), 200 );
}

// ============================================================================
// REFINEMENT ENDPOINTS
// ============================================================================

function tec_list_refinements( $request ) {
    $limit = intval( $request->get_param( 'limit' ) ) ?: 10;
    $limit = min( $limit, 50 );

    $refinements = get_option( 'tec_codex_refinements', array() );
    $refinements = array_slice( $refinements, 0, $limit );

    return new WP_REST_Response( array(
        'entries' => $refinements,
        'count' => count( $refinements ),
    ), 200 );
}

function tec_log_refinement( $request ) {
    $body = json_decode( $request->get_body(), true );

    $refinement = array(
        'id' => current_time( 'mysql' ) . '-' . wp_generate_uuid4(),
        'question' => sanitize_text_field( $body['question'] ?? '' ),
        'response_summary' => sanitize_textarea_field( $body['response_summary'] ?? '' ),
        'actionable_insight' => sanitize_textarea_field( $body['actionable_insight'] ?? '' ),
        'new_idea' => sanitize_textarea_field( $body['new_idea'] ?? '' ),
        'card_references' => array_map( 'sanitize_text_field', $body['card_references'] ?? array() ),
        'timestamp' => current_time( 'c' ),
        'source' => sanitize_text_field( $body['source'] ?? 'api' ),
        'tags' => array_map( 'sanitize_text_field', $body['tags'] ?? array() ),
    );

    $refinements = get_option( 'tec_codex_refinements', array() );
    array_unshift( $refinements, $refinement );
    $refinements = array_slice( $refinements, 0, 100 ); // Keep last 100
    update_option( 'tec_codex_refinements', $refinements );

    return new WP_REST_Response( array(
        'entry' => $refinement,
    ), 201 );
}
