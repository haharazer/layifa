<?php
/**
 * Created by PhpStorm.
 * User: MyPC
 * Date: 2015/8/15
 * Time: 22:17
 */

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use DB;

class SearchController extends Controller {
    public static function index(Request $request)
    {
        $query = $request->input('query');
        $page = $request->input('page', 1);

        $pageSize = 12;
        $offset = ($page - 1) * $pageSize;
        $items = DB::table('discounts')
            ->where('title', 'like', "%$query%")
            ->skip($offset)
            ->take($pageSize)
            ->orderBy('created_at', 'desc')
            ->get();
        return view('search', ['title' => '搜索', 'items'=> $items, 'page' => $page, 'query' => $query]);
    }
} 